import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import Database from 'better-sqlite3'

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

ipcMain.handle('sqlite:getDevices', async (_, filePath: string) => {
  const db = new Database(filePath);
  try {
    const rows = db.prepare(`
      SELECT ipAddress,hostnames FROM hosts
    `).all();
    return rows;
    } finally {
    db.close();
  }
});

ipcMain.handle('sqlite:getDeviceVulnerabilities', async (_, filePath: string, selectedDevice: string) => {
  if (!selectedDevice) return [];

  const devicedb = new Database(filePath);
  try {
    const devicestatement = devicedb.prepare(`
      SELECT hosts.hostId,hosts.hostnames,services.serviceName,vulnerabilities.cveId FROM hosts 
      JOIN services ON hosts.hostId = services.hostId 
      JOIN vulnerabilities ON vulnerabilities.serviceId = services.serviceId 
      WHERE hosts.ipAddress = ?
    `)
    const rows = devicestatement.all(selectedDevice);
    return rows;
  } finally {
    devicedb.close();
  }
});

function createWindow(): void {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 900,
    height: 670,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
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
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
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
