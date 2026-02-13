import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import path from 'path'
import fs from 'fs'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import Database from 'better-sqlite3'
import {spawn} from "child_process"
import os from "os"
import { randomUUID } from "crypto";
import { downloadFileToCacheDir } from "@huggingface/hub";
import {Template} from "@huggingface/jinja"
import {sendStatus} from "./ipcStatus";

let getLlama: typeof import("node-llama-cpp").getLlama;
let LlamaChatSession: typeof import("node-llama-cpp").LlamaChatSession;

async function loadLLMImports() {
  const llamaCpp = await import("node-llama-cpp");
  getLlama = llamaCpp.getLlama;
  LlamaChatSession = llamaCpp.LlamaChatSession;
}

let session: any;

async function initLlamaModel() {
  const {modelPath, loraPath} = await ensureQwenDownloaded();

  const llama = await getLlama();

  // load the model from disk
  const model = await llama.loadModel({ modelPath });

  // create a context (session state for generation)
  const context = await model.createContext({
    contextSize: "auto",
    threads: 0,
    lora:{
      adapters: [
        {
          filePath: loraPath,
          scale: 4.0
        }
      ]
    }
  });

  return context;
}

async function initAI() {
  const context = await initLlamaModel();

  session = new LlamaChatSession({
    contextSequence: context.getSequence(),
    systemPrompt: `
    You are an expert network diagnostic assistant helping home users identify devices on their network.

    Given Nmap scan data, your goal is to identify the SPECIFIC device model.

    CORE PROTOCOL:
    1. START with a <think> block to analyze the data.
    2. DETERMINE if the device is specific (e.g. \"OnePlus 10 Pro\") or generic (e.g. \"OnePlus Technology\").
    3. END with EXACTLY ONE of the following tags:

    [OPTION 1: IDENTIFIED]
    If you are 90% certain of the specific model:
    <device>Exact Model Name</device>

    [OPTION 2: AMBIGUOUS]
    If you are NOT certain or need user confirmation:
    <question>The clarifying question you want to ask the user</question>

    CRITICAL RULES:\n- NEVER use <device> and <question> in the same response.
    - NEVER output plain text outside of tags.
    `
  });
}

ipcMain.handle("llama:askPing", async (_event, question: string) => {
  if (!session) throw new Error("AI not ready");

  const reply = await session.prompt(question);
  
  return reply;
});

ipcMain.handle("llama:analyzeScanDevices", async (_, scanId: string) => {
  if (!session) throw new Error ("AI not ready");

  const dbPath = path.join(app.getPath("userData"), "networkscans.db");
  const db = new Database(dbPath);

  try {
    const devices = db.prepare(`
    SELECT hostId, ipAddress, macAddress, macVendor, hostnames, inferOs
    FROM hosts
    WHERE scanId = ?
    `).all(scanId);

    const total = devices.length;

    sendStatus("scan:status", {
      phase: "Ping analysis",
      message: `Ping is starting analysis on (${total} devices)`
    });

    for (let i = 0; i < total; i++) {
      const device = devices[i];

      sendStatus("scan:status", {
        phase: "Ping analysis",
        message: `Analyzing ${device.ipAddress} (${i + 1}/${total})`
      })

      const parsedHostnames = device.hostnames
      ? JSON.parse(device.hostnames)
      : [];

      const parsedOsData = device.inferOs
      ? JSON.parse(device.inferOs)
      : [];

      const services = db.prepare(`
        SELECT serviceId as service_id,
          port as port_number,
          protocol,
          state,
          serviceName as name,
          serviceProduct as product,
          serviceVersion as version
        FROM services
        WHERE hostId = ?
      `).all(device.hostId);

      const renderedPrompt = deviceTemplate.render({
        ip_address: device.ipAddress,
        mac_address: device.macAddress,
        mac_vendor: device.macVendor,
        hostnames: parsedHostnames,
        nmap_os_data: JSON.stringify(parsedOsData, null, 2),
        services
      });

      const reply = await session.prompt(renderedPrompt, {
        temperature: 0,
        top_k: 1,
        repeatPenalty: {
          penalty: 1.0,
        }
      });

      const timestamp = Math.floor(Date.now() / 1000);

      db.prepare(`
        INSERT INTO llm (hostId, interType, content, timestamp)
        VALUES (?, ?, ?, ?)
      `).run(device.hostId, "device-identification", reply, timestamp)
      }

      return {success: true};

  } finally {
    db.close();
  }
});

ipcMain.handle("dialog:openSQLiteFile", async () => {
  const { canceled, filePaths } = await dialog.showOpenDialog({
    filters: [{name: 'SQLite Files', extensions: ['sqlite', 'db']}],
    properties: ["openFile"],
  });
  if (canceled) {
    return null;
  } else {
    return filePaths[0];
  }
})

ipcMain.handle('sqlite:getScans', async (_, filePath: string) => {
  console.log('[SQLite] Opening database at:', filePath);
  const db = new Database(filePath);
  try {
    const rows = db.prepare(`
      SELECT scanId,startTime FROM scan
    `).all();
    return rows;
  } finally {
    db.close();
  }
});

ipcMain.handle('sqlite:getDevices', async (_, filePath: string, selectedScan: string) => {
  const db = new Database(filePath);
  try {
    const allDevicesStatement = db.prepare(`
      SELECT ipAddress,hostnames
      FROM hosts
      WHERE scanId = ?
    `)
    const rows = allDevicesStatement.all(selectedScan);
    return rows;
  } finally {
    db.close();
  }
});

ipcMain.handle('sqlite:getDeviceRecommendations', async (_, filePath: string, selectedDevice: string) => {
  if (!selectedDevice) return [];

  const devicedb = new Database(filePath);
  try {
    const devicestatement = devicedb.prepare(`
      SELECT hosts.hostId,hosts.hostnames,llm.interType,llm.content
      FROM hosts 
      JOIN llm ON hosts.hostId = llm.hostId
      WHERE hosts.ipAddress = ?
    `)
    const rows = devicestatement.all(selectedDevice);
    return rows;
  } finally {
    devicedb.close();
  }
});

async function ensureQwenDownloaded() {
  const modelPath  = await downloadFileToCacheDir({
    repo: "ggml-org/Qwen3-1.7B-GGUF",
    path: "Qwen3-1.7B-f16.gguf"
  });

  const loraPath = await downloadFileToCacheDir({
    repo: "dzur658/ping-device-id-LoRA-001-GGUF",
    path: "adapter_model.gguf"
  });

  console.log("Model path:", modelPath);
  console.log("LoRA path:", loraPath);

  return { modelPath, loraPath };
}

function createTempNmapXmlPath() {
  const filename = `nmap-${randomUUID()}.xml`;
  return path.join(os.tmpdir(), filename)
}

function createTempNmapJsonPath() {
  const filename = `nmap-${randomUUID()}.json`;
  return path.join(os.tmpdir(), filename)
}

function getNmapPath() {
  const platform = os.platform();

  if (platform === "win32") {
    return "C:\\Program Files (x86)\\Nmap\\nmap.exe";
  } else {
    return "nmap";
  }
}

ipcMain.handle("nmap:startScan", async (_, ipRange: string) => {
  return new Promise<string>((resolve, reject) => {
    const xmlPath = createTempNmapXmlPath();
    const nmapPath = getNmapPath();

    const scriptsDirectory = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'python', 'scripts')
    : path.join(app.getAppPath(), 'resources', 'python', 'scripts')

    const scriptPaths = [
      'vulscan.nse',
      'console-detect-ouis.nse',
      'echo-detect-ouis.nse',
      'roku-detect-ouis.nse',
      'router-detect-ouis.nse',
      'camera-detect-ouis.nse'
    ].map(file => path.join(scriptsDirectory, file)).join(',');

    const nmapArgs = [
      "--script",
      scriptPaths,
      "-sC", "-O", "-sV", "-vv", 
      "-oX", xmlPath,
      ipRange
    ];

    sendStatus("nmap:status", {
      phase: "starting",
      message: "Starting Nmap scan"
    })

    const proc = spawn(nmapPath, nmapArgs)

    proc.stdout.on("data", (buf) => {
      const text = buf.toString();

      if (text.includes("Initiating Ping Scan")) {
        sendStatus("nmap:status", {phase: "ping", message: "Ping scan"});
      } else if (text.includes("Initiating SYN Stealth Scan")) {
        sendStatus("nmap:status", {phase: "ports", message: "Port scan"});
      } else if (text.includes("Initiating Service scan")) {
        sendStatus("nmap:status", {phase: "services", message: "Service detection"});
      }

      sendStatus("nmap:log", text);
    });

    proc.stderr.on("data", (buf) => {
      sendStatus("nmap:log", buf.toString());
    })

    proc.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(`Nmap exited with ${code}`));
        return;
      }

      sendStatus("nmap:status", {
        phase: "complete",
        message: "Nmap scan complete"
      });

      resolve(xmlPath);
    })
  });
});

ipcMain.handle("nmap:scanLocalDevice", async () => {
  const ip = getLocalIPv4();

  return ip;
})

ipcMain.handle("nmap:scanLocalNetwork", async () => {
  const ip = getLocalIPv4();
  const subnet = getSubnet(ip);

  return subnet;
})

ipcMain.handle("python:processScan", async (_, xmlPath: string) => {
  return new Promise<string>((resolve, reject) => {
    const pythonParserExe = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'python', 'orchestrator.exe')
    : path.join(app.getAppPath(), 'resources', 'python', 'orchestrator.exe');
    
    const jsonPath = createTempNmapJsonPath();
    const dbPath = path.join(app.getPath('userData'), 'networkscans.db');
    console.log(dbPath)

    sendStatus("scan:status", {
      phase: "processing",
      message: "Processing scan results"
    });

    const proc = spawn(pythonParserExe, [
      "--xml-file", xmlPath,
      "--json-file", jsonPath,
      "--db-file", dbPath
    ]);

    proc.stdout.on("data", d =>
      sendStatus("scan:log", d.toString())
    );

    proc.stderr.on("data", d =>
      sendStatus("scan:log", d.toString())
    );

    proc.on("close", (code) => {
      if (code !== 0) {
        reject(new Error("Processing failed"));
        return;
      }

      sendStatus("scan:status", {
        phase: "done",
        message: "Scan processed"
      });

      const db = new Database(dbPath);
      try {
        const row = db.prepare(`
          SELECT scanId FROM scan
          ORDER BY startTime DESC LIMIT 1
        `).get();
        if (!row) reject(new Error("No scan found in DB"));
        else resolve(row.scanId)
      } finally {
        db.close();
      }
    })
  });
});

let deviceTemplate: Template;

function loadTemplate() {
  const templatePath = path.join(
    app.getAppPath(),
    'resources',
    'templates',
    'prompt_template.j2'
  );

  const templateString = fs.readFileSync(templatePath, "utf-8");
  deviceTemplate = new Template(templateString)
}

function createWindow(): void {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 900,
    height: 670,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: path.join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'))
  }
}

function getLocalIPv4() {
  const networkInterfaces = os.networkInterfaces();

  for (const name of Object.keys(networkInterfaces)) {
    for (const networkInterface of networkInterfaces[name] || []) {
      if (networkInterface.family === "IPv4" && !networkInterface.internal) {
        return networkInterface.address;
      }
    }
  }
  throw new Error("No network interfaces found");
}

function getSubnet(ip: string) {
  const parts = ip.split(".");
  return `${parts[0]}.${parts[1]}.${parts[2]}.0/24`;
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then((async () => {
  const userData = app.getPath('userData');
  const dbPath = path.join(userData, 'networkscans.db');

  const seedDBPath = path.join(
    app.getAppPath(),
    'src',
    'renderer',
    'public',
    'networkscans.db'
  );

  if (!fs.existsSync(dbPath)) {
    if (!fs.existsSync(seedDBPath)) {
      throw new Error(`Seed DB missing: ${seedDBPath}`);
    }
    fs.copyFileSync(seedDBPath, dbPath);
    console.log('[DB] Seeded databse to:', dbPath)
  }

  ipcMain.handle('database:getPath', () => dbPath);

  loadTemplate();

  // Set app user model id for windows
  electronApp.setAppUserModelId('com.electron')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  createWindow()

  // await ensureQwenDownloaded().catch(err =>
  //   console.error("Model download failed:", err)
  // );

  await loadLLMImports();
  await initLlamaModel();
  await initAI();

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
}))

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
