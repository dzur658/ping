import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./components/HomePage";
import ScanOptionsPage from "./components/ScanOptionsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/ScanOptionsPage" element={<ScanOptionsPage />} />
      </Routes>
    </Router>
  );
}

export default App
