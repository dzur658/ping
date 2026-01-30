import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld("electronAPI", {
  getDBPath: () => ipcRenderer.invoke('database:getPath'),
  openSQLiteFile: () => ipcRenderer.invoke("dialog:openSQLiteFile"),
  getScans: (filePath: string) => ipcRenderer.invoke("sqlite:getScans", filePath),
  getDevices: (filePath: string, selectedScan: string) => ipcRenderer.invoke("sqlite:getDevices", filePath, selectedScan),
  getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceVulnerabilities", filePath, selectedDevice),
  getDeviceRecommendations: (filePath: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceRecommendations", filePath, selectedDevice),
  scanLocalDevice: () => ipcRenderer.invoke("nmap:scanLocalDevice"),
  scanLocalNetwork: () => ipcRenderer.invoke("nmap:scanLocalNetwork"),
  runScan: (args: string[]) => ipcRenderer.invoke("nmap:runScan", args),
  processScan: (xmlPath: string) => ipcRenderer.invoke("python:processScan", xmlPath),
  askPing: (question: string) => ipcRenderer.invoke("llama:askPing", question)
})
