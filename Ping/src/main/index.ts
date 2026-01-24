import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import path from 'path'
import fs from 'fs'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import Database from 'better-sqlite3'
import {execFile} from "child_process"
import os from "os"
import { randomUUID } from "crypto";

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

// ipcMain.handle('sqlite:getDeviceVulnerabilities', async (_, filePath: string, selectedDevice: string) => {
//   if (!selectedDevice) return [];

//   const devicedb = new Database(filePath);
//   try {
//     const devicestatement = devicedb.prepare(`
//       SELECT hosts.hostId,hosts.hostnames,services.serviceName,vulnerabilities.cveId
//       FROM hosts 
//       JOIN services ON hosts.hostId = services.hostId 
//       JOIN vulnerabilities ON vulnerabilities.serviceId = services.serviceId 
//       WHERE hosts.ipAddress = ?
//     `)
//     const rows = devicestatement.all(selectedDevice);
//     return rows;
//   } finally {
//     devicedb.close();
//   }
// });

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

function createTempNmapXmlPath() {
  const filename = `nmap-${randomUUID()}.xml`;
  return path.join(os.tmpdir(), filename)
}

ipcMain.handle("nmap:runScan", async (_, args: string[]) => {
  return new Promise<string>((resolve, reject) => {
    const xmlPath = createTempNmapXmlPath();
    const nmapArgs = [
      ...args,
      "-oX",
      xmlPath
    ]

    execFile(
      "nmap",
      nmapArgs,
      {maxBuffer: 10 * 1024 * 1024},
      (error, stdout, stderr) => {
        if (error) {
          reject(stderr || error.message);
          return;
        }
        resolve(xmlPath);
      }
    );
  });
});

ipcMain.handle("nmap:scanLocalDevice", async () => {
  const ip = getLocalIPv4();

  return {
    target: ip,
    args: ["-sV", ip]
  }
})

ipcMain.handle("nmap:scanLocalNetwork", async () => {
  const ip = getLocalIPv4();
  const subnet = getSubnet(ip);

  return {
    target: subnet,
    args: ["-sn", subnet]
  }
})

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
app.whenReady().then(() => {
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

  // Set app user model id for windows
  electronApp.setAppUserModelId('com.electron')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

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
