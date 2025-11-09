import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld("electronAPI", {
  openSQLiteFile: () => ipcRenderer.invoke("dialog:openSQLiteFile"),
  getDevices: (filePath: string) => ipcRenderer.invoke("sqlite:getDevices", filePath),
  getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceVulnerabilities", filePath, selectedDevice)
})