type NmapScanRequest = {
  target: string;
  args: string[];
}

interface Window {
  electronAPI: {
    getDBPath(): Promise<string>;
    openSQLiteFile: () => Promise<string | null>;
    getScans: (filePath: string) => Promise<any[]>;
    getDevices: (filePath: string, selectedScan: string) => Promise<any[]>;
    getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => Promise<any[]>;
    getDeviceRecommendations: (filePath: string, selectedDevice: string) => Promise<any[]>;
    askPing: (question: string) => Promise<string>;
    scanLocalDevice: () => Promise<NmapScanRequest>;
    scanLocalNetwork: () => Promise<NmapScanRequest>;
    runScan: (args: string[]) => Promise<string>;
    processScan: (args: string) => Promise<string>;
  };
}