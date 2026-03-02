type ScanPhase = 
  | "starting"
  | "ping"
  | "ports"
  | "services"
  | "scripts"
  | "processing"
  | "complete"
  | "done"
  | "error";

interface ScanStatus {
  phase: ScanPhase;
  message: string;
  percent?: number;
}

interface Window {
  electronAPI: {
    getDBPath(): Promise<string>;
    openSQLiteFile: () => Promise<string | null>;
    getScans: (filePath: string) => Promise<{scanId: string; startTime: string;}[]>;
    getDevices: (filePath: string, selectedScan: string) => Promise<any[]>;
    getDeviceVulnerabilities: (filePath: string, selectedDevice: string) => Promise<{filePath: string; selectedDevice: string;}[]>;
    getDeviceRecommendations: (filePath: string, scanId: string, selectedDevice: string) => Promise<{hostId: string; hostnames: string; interType: string; content: string;}[]>;
    
    askPing: (question: string) => Promise<string>;
    askFollowup: (question: string, deviceName: string, deviceId: string, historyContent?: string) => Promise<string>;
    analyzeScanDevices: (scanId: string) => Promise<string>;

    scanLocalDevice: () => Promise<string>;
    scanLocalNetwork: () => Promise<string>;
    startScan: (ipRange: string) => Promise<string>;
    processScan: (args: string) => Promise<string>;

    onNmapStatus(callback: (status: ScanStatus) => void): () => void;
    onProcessScanStatus(callback: (status: ScanStatus) => void): () => void;
    onLog(callback: (message: string) => void): () => void;

    onRefreshData(callback: (command: DBCommand) => void): () => void;
  };
}