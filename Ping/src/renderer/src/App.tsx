import { useState, useEffect } from "react";
import {HashRouter as Router, Routes, Route, useNavigate} from "react-router-dom";
import HomePage from "./pages/HomePage";
import ModelDownloadPage from "./pages/ModelDownloadPage";
import ScanSelectionPage from "./pages/ScanSelectionPage";
import ReportPage from "./pages/ReportPage";
import ScanOptionsPage from "./pages/ScanOptionsPage";

function AppRoutes() {
  const [filePath, setFilePath] = useState<string | null>(null);
  const [selectedScan, setSelectedScan] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    window.electronAPI.checkModelStatus().then((status) => {
      if (!status.deviceIDReady || !status.technicalAssistantReady) {
        navigate('/ModelDownloadPage');
      }
    });
  }, []);

  return (
      <Routes>
        <Route path="/" element={<HomePage setFilePath={setFilePath}/>} />
        <Route path="/ModelDownloadPage" element={<ModelDownloadPage/>} />
        <Route path="/ScanSelectionPage" element={<ScanSelectionPage filePath={filePath} setSelectedScan={setSelectedScan}/>} />
        <Route path="/ReportPage" element={<ReportPage filePath={filePath} selectedScan={selectedScan}/>} />
        <Route path="/ScanOptionsPage" element={<ScanOptionsPage/>} />
      </Routes>
  );
}

function App() {
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
}

export default App;
