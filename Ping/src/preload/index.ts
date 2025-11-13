import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld("electronAPI", {
  openSQLiteFile: () => ipcRenderer.invoke("dialog:openSQLiteFile"),
  getScans: (filePath: string) => ipcRenderer.invoke("sqlite:getScans", filePath),
  getDevices: (filePath: string, selectedScan: string) => ipcRenderer.invoke("sqlite:getDevices", filePath, selectedScan),
  getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceVulnerabilities", filePath, selectedDevice)
})