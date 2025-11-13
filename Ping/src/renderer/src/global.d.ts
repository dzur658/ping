interface Window {
  electronAPI: {
    openSQLiteFile: () => Promise<string | null>;
    getScans: (filePath: string) => Promise<any[]>;
    getDevices: (filePath: string, selectedScan: string) => Promise<any[]>;
    getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => Promise<any[]>;
  };
}