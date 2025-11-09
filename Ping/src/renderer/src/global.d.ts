interface Window {
  electronAPI: {
    openSQLiteFile: () => Promise<string | null>;
    getDevices: (filePath: string) => Promise<any[]>;
    getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => Promise<any[]>;
  };
}