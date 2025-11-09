import { useState } from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/HomePage";
import ReportPage from "./pages/ReportPage";
import ScanOptionsPage from "./pages/ScanOptionsPage";

function App() {
  const [filePath, setFilePath] = useState<string | null>(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage setFilePath={setFilePath}/>} />
        <Route path="/ReportPage" element={<ReportPage filePath={filePath}/>} />
        <Route path="/ScanOptionsPage" element={<ScanOptionsPage/>} />
      </Routes>
    </Router>
  );
}

export default App
