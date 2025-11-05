interface Window {
  electronAPI: {
    openFileDialog: () => Promise<string | null>;
  };
}