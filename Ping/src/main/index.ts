import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import path from 'path'
import fs from 'fs'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import Database from 'better-sqlite3'
import {spawn, exec} from "child_process"
import os from "os"
import { randomUUID } from "crypto";
import {Template} from "@huggingface/jinja"
import {sendStatus} from "./ipcStatus";
import {promisify} from "util"
import PingLogo from '../../resources/PingLogo.png?asset'

let mainWindow: BrowserWindow | null = null;
let llamaServerProcess: any;
let deviceIDModelPath: string;
let technicalAssistantModelPath: string;
let currentModelPath: string | null;
let isDownloading = false;

const execAsync = promisify(exec);

async function detectGPU(): Promise<{ hasNvidia: boolean, hasAMD: boolean}> {
  try {
    const {stdout} = await execAsync("wmic path win32_VideoController get name");
    const lower = stdout.toLowerCase();
    return {
      hasNvidia: lower.includes("nvidia"),
      hasAMD: lower.includes("amd") || lower.includes("radeon")
    };
  } catch {
    return {hasNvidia: false, hasAMD: false}
  }
}

async function switchModel(modelPath: string) {
  console.log(currentModelPath)
  console.log(modelPath)
  if (currentModelPath === modelPath && llamaServerProcess) {
    return;
  }

  if (llamaServerProcess) {
    console.log("Killing old Llama server...");
    llamaServerProcess.kill();
    llamaServerProcess = null;
  }

  const {hasNvidia, hasAMD} = await detectGPU();
  const useGPU = hasNvidia || hasAMD;

  const totalRamGB = os.totalmem() / (1024 ** 3)
  const totalCores = os.cpus().length;
  //const threadsToUse = Math.max(1, Math.floor(totalCores / 2))
  const ctxSize = totalRamGB < 8 ? 2048 : 4096
  const ubatchSize = totalCores <= 4? 8 : 16

  return new Promise((resolve, reject) => {
    const serverExe = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', useGPU ? 'llama-cpp-gpu' : 'llama-cpp-cpu', 'llama-server.exe')
    : path.join(app.getAppPath(), 'resources', useGPU ? 'llama-cpp-gpu' : 'llama-cpp-cpu', 'llama-server.exe');

    const args = [
      '--model', modelPath,
      '--port', '3500',
      '--ctx-size', String(ctxSize),
      '--parallel', '1'
    ]

    if (useGPU) {
      args.push('--n-gpu-layers', '99');
      args.push('--threads', '2');
      args.push('--ubatch-size', '512');
    } else {
      args.push('--threads', '4');
      args.push('--ubatch-size', String(ubatchSize));
      args.push('--no-mmap');
    }

    llamaServerProcess = spawn(serverExe, args, {
      windowsHide: true,
      detached: false,
      stdio: ['ignore', 'pipe', 'pipe']
    });

    const logPath = path.join(app.getPath('userData'), 'ping-debug.log');
    const writeLog = (msg: string) => fs.appendFileSync(logPath, `[${new Date().toISOString()}] ${msg}\n`);

    llamaServerProcess.stderr?.on('data', (data: Buffer) => {
        const log = data.toString();
        writeLog(`[stderr] ${log}`);
        if (log.includes('main: server is listening')) {
            currentModelPath = modelPath;
            writeLog('Server ready!');
            resolve(true);
        }
    });

    llamaServerProcess.stdout?.on('data', (data: Buffer) => {
        writeLog(`[stdout] ${data.toString()}`);
    });

    llamaServerProcess.on('close', (code: number) => {
        writeLog(`Server closed with code: ${code}`);
        if (code !== 0 && currentModelPath !== modelPath) {
            reject(new Error(`Llama server exited with code ${code}`));
        }
    });

    llamaServerProcess.on('error', (err: any) => {
        writeLog(`Spawn error: ${err.message}`);
        reject(err);
    });

    llamaServerProcess.stderr?.on('data', (data: Buffer) => {
      const log = data.toString();
      console.log(log);

      if (log.includes('main: server is listening')) {
        currentModelPath = modelPath;
        console.log("Llama Server is ready on port 3500");
        resolve(true)
      }
    });

    llamaServerProcess.on('error', (err: any) => reject(err));
  });
}

async function initModels() {
  const modelsDirectory = path.join(app.getPath('userData'), 'models');
  if (!fs.existsSync(modelsDirectory)) {
    fs.mkdirSync(modelsDirectory, {recursive: true});
  }

  deviceIDModelPath = path.join(modelsDirectory, 'ping_device_id.gguf')
  technicalAssistantModelPath = path.join(modelsDirectory, 'ping_technical_support.gguf')
}

async function downloadModelWithProgress(
  url: string,
  destinationPath: string,
  modelKey: string
): Promise<void> {
  const tempPath = destinationPath + '.tmp';

  const response = await fetch(url, {redirect: 'follow'});
  if (!response.ok) throw new Error(`Download failed: ${response.status}`);

  const total = parseInt(response.headers.get('content-length') || '0');
  let downloaded = 0;
  let lastReportedPercent = -1;

  const fileStream = fs.createWriteStream(tempPath);
  const reader = response.body!.getReader();

  while (true) {
    const {done, value} = await reader.read();
    if (done) break;
    fileStream.write(Buffer.from(value));
    downloaded += value.length

    const percent = total ? Math.round((downloaded / total) * 100) : 0;

    if (percent !== lastReportedPercent) {
      lastReportedPercent = percent;
      mainWindow?.webContents.send('models:progress', {
        modelKey,
        downloaded,
        total,
        percent: total ? Math.round((downloaded / total) * 100) :0
      });
    }
  }

  await new Promise<void>((resolve, reject) => {
    fileStream.end();
    fileStream.on('finish', resolve);
    fileStream.on('error', reject);
  })

  fs.renameSync(tempPath, destinationPath);
}

function extractTaggedValue(text: string) {
  const deviceTagMatch = text.match(/<device>(.*?)<\/device>/);
  if (deviceTagMatch) {
    return {
      type: "device",
      value: deviceTagMatch[1].trim()
    }
  }

  const questionTagMatch = text.match(/<question>(.*?)<\/question>/);
  if (questionTagMatch) {
    return {
      type: "question",
      value: questionTagMatch[1].trim()
    }
  }

  return null;
}

ipcMain.handle('models:checkStatus', () => {
  return {
    deviceIDReady: fs.existsSync(deviceIDModelPath),
    technicalAssistantReady: fs.existsSync(technicalAssistantModelPath)
  };
});

ipcMain.handle('models:startDownload', async () => {
  if (isDownloading) return;
  isDownloading = true

  try {
    if (!fs.existsSync(deviceIDModelPath)) {
      await downloadModelWithProgress(
        'https://huggingface.co/dzur658/ping-device-id-fused-gguf-001/resolve/main/ping_device_id.gguf',
        deviceIDModelPath,
        'deviceID'
      );
    }

    if (!fs.existsSync(technicalAssistantModelPath)) {
      await downloadModelWithProgress(
        'https://huggingface.co/dzur658/ping-technical-assistant-fused-gguf-001/resolve/main/ping_technical_support.gguf',
        technicalAssistantModelPath,
        'technicalAssistant'
      );
    }

    await switchModel(deviceIDModelPath);
    mainWindow?.webContents.send('models:downloadComplete');
  } catch (err: any) {
    mainWindow?.webContents.send('models:downloadError', err.message)
  } finally {
    isDownloading = false;
  }
})

ipcMain.handle("llama:analyzeScanDevices", async (_, scanId: string) => {
  try {
    await switchModel(deviceIDModelPath);
  } catch (e) {
    console.error("Failed to start deviceID LLM:", e)
  }

  const dbPath = path.join(app.getPath("userData"), "networkscans.db");
  const db = new Database(dbPath);
  const knowledgeBasePath = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'knowledgeBase', 'knowledge_base.db')
    : path.join(app.getAppPath(), 'resources', 'knowledgeBase', 'knowledge_base.db');
  const knowledgeBaseDB = new Database(knowledgeBasePath)
  
  const systemPrompt = `
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
  `;

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

      try {
        const messages = [
          {role: "system", content: systemPrompt},
          {role: "user", content: renderedPrompt}
        ]

        const response = await fetch("http://localhost:3500/v1/chat/completions", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            stream: false,
            messages,
            temperature: 0.3
          })
        });

        const data = await response.json()
        const reply = data.choices[0].message.content;

        messages.push({role: "assistant", content: reply})

        let deviceKnowledgeRow;

        const timestamp = Math.floor(Date.now() / 1000);
        const extractedTagValue = extractTaggedValue(reply);

        if (extractedTagValue?.type === "device") {
          const deviceKnowledgeQuery = knowledgeBaseDB.prepare(`
            SELECT documentation
            FROM knowledge
            WHERE device_name = ?
          `)
          deviceKnowledgeRow = deviceKnowledgeQuery.get(extractedTagValue.value);
          if (deviceKnowledgeRow) {
            const knowledgeContent = deviceKnowledgeRow.documentation

            db.prepare(`
              UPDATE hosts
              SET Identified = ?
              WHERE hostId = ?
            `).run(extractedTagValue.value, device.hostId)

            db.prepare(`
              INSERT OR REPLACE INTO llm (hostId, interType, content, timestamp)
              VALUES (?, ?, ?, ?)
            `).run(device.hostId, "device-summary", knowledgeContent, timestamp)
          }
        } else {
          db.prepare(`
            INSERT OR REPLACE INTO llm (hostId, interType, content, timestamp)
            VALUES (?, ?, ?, ?)
          `).run(device.hostId, "device-identification", JSON.stringify(messages), timestamp)
        }

      } catch (innerError) {
        console.error(`Failed to analyze device ${device.ipAddress}:`, innerError);
      }
    }

    return {success: true};
  } finally {
    db.close();
    knowledgeBaseDB.close();
  }
});

ipcMain.handle("llama:askFollowup", async (_event, question, deviceId,) => {
  try {
    await switchModel(deviceIDModelPath);
  } catch (e) {
    console.error("Failed to start deviceID LLM:", e)
  }

  const dbPath = path.join(app.getPath("userData"), "networkscans.db");
  const db = new Database(dbPath);

  const history = db.prepare(`
    SELECT content
    FROM llm
    WHERE hostId = ?  
  `).get(deviceId)

  if (!history.content) {
    throw new Error(`No history found for device ${deviceId}`)
  }

  const messages = JSON.parse(history.content)

  messages.push({role: "user", content: question})

  const response = await fetch("http://localhost:3500/v1/chat/completions", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      stream: false,
      messages,
      temperature: 0.3
    })
  });

  if (!response.ok) {
    const errText = await response.text();
    console.error("Llama server error:", response.status, errText);
    throw new Error(`Llama server returned ${response.status}: ${errText}`);
  }

  const data = await response.json()
  const reply = data.choices[0].message.content;

  messages.push({role: "assistant", content: reply})

  const timestamp = Math.floor(Date.now() / 1000);

  db.prepare(`
    INSERT OR REPLACE INTO llm (hostId, interType, content, timestamp)
    VALUES (?, ?, ?, ?)
  `).run(deviceId, "device-identification", JSON.stringify(messages), timestamp)

  let deviceKnowledgeRow

  const extractedTagValue = extractTaggedValue(reply);

  if (extractedTagValue?.type === "device") {
    console.log(extractedTagValue.value)
    const knowledgeBasePath = app.isPackaged
      ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'knowledgeBase', 'knowledge_base.db')
      : path.join(app.getAppPath(), 'resources', 'knowledgeBase', 'knowledge_base.db');
    const knowledgeBaseDB = new Database(knowledgeBasePath)

    try {
      db.prepare(`
        UPDATE hosts
        SET Identified = ?
        WHERE hostId = ?
      `).run(extractedTagValue.value, deviceId)
      
      const deviceKnowledgeQuery = knowledgeBaseDB.prepare(`
        SELECT documentation
        FROM knowledge
        WHERE device_name = ?
      `)
      deviceKnowledgeRow = deviceKnowledgeQuery.get(extractedTagValue.value);
    } finally {
      knowledgeBaseDB.close();
    }

    if (deviceKnowledgeRow) {
      const knowledgeContent = deviceKnowledgeRow.documentation
      db.prepare('DELETE FROM llm WHERE hostId = ?').run(deviceId);
      db.prepare(`
        INSERT OR REPLACE INTO llm (hostId, interType, content, timestamp)
        VALUES (?, ?, ?, ?)
      `).run(deviceId, "device-summary", knowledgeContent, timestamp)
      sendStatus("db:refresh", {
        phase: "Database refresh",
        message: "Refreshing db results"
      });
    }
  } else {
    console.log("Not ID'd")
  }

  return reply;
});

ipcMain.handle("llama:askPing", async (_event, question, deviceId) => {
  try {
    await switchModel(technicalAssistantModelPath);
  } catch (e) {
    console.error("Failed to start technical assistant LLM:", e)
  }

  const dbPath = path.join(app.getPath("userData"), "networkscans.db");
  const db = new Database(dbPath);

  try {
    const deviceTag = db.prepare(`
      SELECT Identified
      FROM hosts
      WHERE hostId = ?  
    `).get(deviceId)

    const history = db.prepare(`
      SELECT content, interType
      FROM llm
      WHERE hostId = ?  
    `).get(deviceId)

    if (!history.content) {
      throw new Error(`No history found for device ${deviceId}`)
    }

    const systemPrompt = `You are a helpful, patient technical support assistant. Your role is to assist non-technical users with their devices and technology problems.

      Key guidelines:
      - Be friendly and supportive
      - Explain things in simple, clear language
      - Avoid technical jargon when possible
      - If a user seems confused, break down instructions into smaller steps
      - Be patient with users who are less tech-savvy
      - Acknowledge their frustration and reassure them
      - Provide step-by-step instructions when needed
      - Be encouraging throughout conversation
      - Never make the user feel stupid for asking basic questions
      - If you're not sure about something, be honest
      - Remain temporally neutral when recommending hardware or software versions, refer to product lines and software lifecycles rather than specific years or dates.
      - Never mention the specific date or year

      Remember that your users are not technical experts. They may be elderly, busy, or just unfamiliar with technology. Your goal is to help them solve their problem while making them feel supported and understood.

      IMPORTANT: You must always output your internal reasoning before your response.
      Your reasoning must be substantive and useful - analyze what the user is asking, what information you have, and plan your explanation.
      NEVER use generic placeholders like "thinking through request" or "considering the question" - if you cannot generate substantive reasoning, express uncertainty instead.

      Example of GOOD reasoning:
      "The user is asking about updating their iPhone 6. I need to check if iOS 15 is still supported for this device and provide clear steps for updating. The user seems elderly based on their questions, so I should use very simple language and break down each step."

      Example of BAD reasoning:
      "I am thinking about their request. Let me consider what to say."

      Use the following format:


      [Your actual response to the user follows here]

      Refuse to directly answer questions requiring real-time data or specific product recommendations based on the current date.`

    let messages;

    if (history.interType === "device-summary") {
      messages = [
        {role: "system", content: systemPrompt},
        {role: "user", content: `[System Command]: Load reference for ${deviceTag.Identified}`},
        {role: "assistant", content: `<think>\nTrigger: System Command received (\"Load reference for {device_str}\").\nAction: Retrieve \"{device_str} Update Guide\" from database.\nPlan: Output the full update instructions so the user has the context available immediately.\n</think> \n${history.content}`},
      ]
      
      db.prepare(`
        UPDATE llm
        SET interType = ?
        WHERE hostId = ?
      `).run("device-technical", deviceId)
    } else if (history.interType === "device-technical") {
      try {
        messages = JSON.parse(history.content)
      } catch {
        messages = [
          {role: "system", content: systemPrompt},
          {role: "user", content: `[System Command]: Load reference for ${deviceTag.Identified}`},
          {role: "assistant", content: `<think>\nTrigger: System Command received (\"Load reference for {device_str}\").\nAction: Retrieve \"{device_str} Update Guide\" from database.\nPlan: Output the full update instructions so the user has the context available immediately.\n</think> \n${history.content}`},
        ]
        db.prepare(`
          UPDATE llm
          SET interType = ?
          WHERE hostId = ?
        `).run("device-technical", deviceId)
      }
    }

    messages.push({role: "user", content: question})

    const response = await fetch("http://localhost:3500/v1/chat/completions", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        stream: false,
        messages,
        temperature: 0.3
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      console.error("Llama server error:", response.status, errText);
      throw new Error(`Llama server returned ${response.status}: ${errText}`);
    }

    const data = await response.json()
    const reply = data.choices[0].message.content;

    messages.push({role: "assistant", content: reply})

    db.prepare(`
      UPDATE llm
      SET content = ?
      WHERE hostId = ?
    `).run(JSON.stringify(messages), deviceId)

    return reply;
  } finally {
    db.close()
  }
})

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

ipcMain.handle('sqlite:getScanStartTime', async (_, filePath: string, scanId: string) => {
  const db = new Database(filePath);
  try {
    const scanStartTime = db.prepare(`
      SELECT startTime
      FROM scan
      WHERE scanId = ?
    `).get(scanId);
    return scanStartTime.startTime;
  } finally {
    db.close();
  }
});

ipcMain.handle('sqlite:getDevices', async (_, filePath: string, selectedScan: string) => {
  const db = new Database(filePath);
  try {
    const allDevicesStatement = db.prepare(`
      SELECT hosts.ipAddress,hosts.hostnames,hosts.hostId,llm.interType
      FROM hosts
      JOIN llm ON hosts.hostId = llm.hostId
      WHERE scanId = ?
      AND llm.timestamp = (
        SELECT MAX(timestamp)
        FROM llm AS llm_inner
        WHERE llm_inner.hostId = hosts.hostId
      )
    `)
    const rows = allDevicesStatement.all(selectedScan);
    return rows;
  } finally {
    db.close();
  }
});

ipcMain.handle('sqlite:getDeviceRecommendations', async (_, filePath: string, scanId: string, selectedDevice: string) => {
  if (!selectedDevice) return [];

  const devicedb = new Database(filePath);
  const knowledgeBasePath = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'knowledgeBase', 'knowledge_base.db')
    : path.join(app.getAppPath(), 'resources', 'knowledgeBase', 'knowledge_base.db');
  const knowledgeBaseDB = new Database(knowledgeBasePath)

  try {
    let deviceInfo
    const devicestatement = devicedb.prepare(`
      SELECT hosts.hostId,hosts.hostnames,hosts.Identified,llm.interType,llm.content
      FROM hosts 
      JOIN llm ON hosts.hostId = llm.hostId
      WHERE hosts.scanId = ?
      AND hosts.ipAddress = ?
    `)
    const deviceRow = devicestatement.get(scanId, selectedDevice);

    if (deviceRow.interType === "device-summary" || deviceRow.interType === "device-technical") {
      const deviceKnowledgeQuery = knowledgeBaseDB.prepare(`
        SELECT documentation
        FROM knowledge
        WHERE device_name = ?
      `)
      const deviceKnowledgeRow = deviceKnowledgeQuery.get(deviceRow.Identified);

      deviceInfo = [{
        interType: deviceRow.interType,
        content: deviceRow.content,
        knowledgeRow: deviceKnowledgeRow.documentation
      }]
    } else {
      deviceInfo = [{
        interType: deviceRow.interType,
        content: deviceRow.content      }]
    }

    return deviceInfo;
  } finally {
    devicedb.close();
    knowledgeBaseDB.close();
  }
});

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
      'pingscan_cpe2json.nse',
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
  const templatePath = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'templates', 'prompt_template.j2')
    : path.join(app.getAppPath(), 'resources', 'templates', 'prompt_template.j2');

  const templateString = fs.readFileSync(templatePath, "utf-8");
  deviceTemplate = new Template(templateString)
}

function createWindow(): void {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 900,
    height: 670,
    title: "Ping",
    icon: PingLogo,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { PingLogo } : {}),
    webPreferences: {
      preload: path.join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow?.show()
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
  app.setName("Ping")
  const userData = app.getPath('userData');
  const dbPath = path.join(userData, 'networkscans.db');

  const seedDBPath = app.isPackaged
    ? path.join(process.resourcesPath, 'app.asar.unpacked', 'resources', 'networkscans.db')
    : path.join(app.getAppPath(), 'resources', 'networkscans.db');

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

  try {
    await initModels();
  } catch (error) {
    console.error('Startup error:', error);
    mainWindow?.show()
  }

  const modelsReady = 
    fs.existsSync(deviceIDModelPath) &&
    fs.existsSync(technicalAssistantModelPath);

  if (modelsReady) {
    try {
      await switchModel(deviceIDModelPath);
    } catch (e) {
      console.error("Failed to start initial LLM:", e)
    }
  }

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
