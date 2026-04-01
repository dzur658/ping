import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld("electronAPI", {
  checkModelStatus: () => ipcRenderer.invoke('models:checkStatus'),
  startModelDownload: () => ipcRenderer.invoke('models:startDownload'),
  onModelProgress: (cb) => {
    const handler = (_event: any, data: any) => cb(data);
    ipcRenderer.on('models:progress', handler)
    return () => ipcRenderer.removeListener('models:progress', handler)
  },
  onModelDownloadComplete: (cb) => {
    const handler = () => cb();
    ipcRenderer.on('models:downloadComplete', handler);
    return () => ipcRenderer.removeListener('models:downloadComplete', handler);
  },
  onModelDownloadError: (cb) => {
    const handler = (_event: any, msg: any) => cb(msg);
    ipcRenderer.on('models:downloadError', handler);
    return () => ipcRenderer.removeListener('models:downloadError', handler);
  },
  getDBPath: () => ipcRenderer.invoke('database:getPath'),
  openSQLiteFile: () => ipcRenderer.invoke("dialog:openSQLiteFile"),
  getScans: (filePath: string) => ipcRenderer.invoke("sqlite:getScans", filePath),
  getScanStartTime: (filePath: string, scanId: string) => ipcRenderer.invoke("sqlite:getScanStartTime", filePath, scanId),
  getDevices: (filePath: string, selectedScan: string) => ipcRenderer.invoke("sqlite:getDevices", filePath, selectedScan),
  getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceVulnerabilities", filePath, selectedDevice),
  getDeviceRecommendations: (filePath: string, scanId: string, selectedDevice: string) => ipcRenderer.invoke("sqlite:getDeviceRecommendations", filePath, scanId, selectedDevice),
  
  askPing: (question: string, deviceId: string) => ipcRenderer.invoke("llama:askPing", question, deviceId),
  askFollowup: (question: string, deviceId: string,) => ipcRenderer.invoke("llama:askFollowup", question, deviceId,),
  analyzeScanDevices: (scanId: string) => ipcRenderer.invoke("llama:analyzeScanDevices", scanId),

  scanLocalDevice: () => ipcRenderer.invoke("nmap:scanLocalDevice"),
  scanLocalNetwork: () => ipcRenderer.invoke("nmap:scanLocalNetwork"),

  startScan: (ipRange: string) => ipcRenderer.invoke("nmap:startScan", ipRange),
  processScan: (xmlPath: string) => ipcRenderer.invoke("python:processScan", xmlPath),

  onNmapStatus: (cb) => {
    const listener = (_event: unknown, data: unknown) => cb(data);
    ipcRenderer.on("nmap:status", listener)
    return () => ipcRenderer.removeListener("nmap:status", listener)
  },

  onProcessScanStatus: (cb) => {
    const listener = (_event: unknown, data: unknown) => cb(data);
    ipcRenderer.on("scan:status", listener)
    return () => ipcRenderer.removeListener("scan:status", listener)
  },

  onLog: (cb) => {
    const listener = (_event: unknown, msg: string) => cb(msg);
    ipcRenderer.on("nmap:log", listener)
    return () => ipcRenderer.removeListener("nmap:log", listener);
  },

  onRefreshData: (cb) => {
    const listener = (_event: unknown, msg: unknown) => cb(msg);
    ipcRenderer.on("db:refresh", listener)
    return () => ipcRenderer.removeListener("db:refresh", listener)
  },
})
