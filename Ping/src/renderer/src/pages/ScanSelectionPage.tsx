import { Box,Typography,} from "@mui/material";
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import BackButton from "../components/BackButton";
import ScanChoice from "../components/ScanChoice";

interface ScanSelectionProps {
    filePath: string | null;
    setSelectedScan: (scanId: string | null) => void;
}

export default function ScanSelection({filePath, setSelectedScan}: ScanSelectionProps) {
    interface Scan {
        scanId: string;
        startTime: string | null;
    }
    
    const [scans, setScans] = useState<Scan[]>([]);
    const [selectedScan, setLocalSelectedScan] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!filePath) {
            navigate("/")
            return;
        }

        const loadScans = async () => {
            const scanList: Scan[] = await window.electronAPI.getScans(filePath);
            setScans(scanList);

            if (scanList.length <= 0) {
                navigate("/")
                return;
            }
        };

        loadScans();
    }, [filePath, navigate])

    // useEffect(() => {
    //     if (!selectedScan || !filePath) return;
    //     setSelectedScan(selectedScan)
    //     navigate("/ReportPage")
    // }, [selectedScan, filePath, navigate]);

    return (
        <Box
            sx={{
                display: "flex",
                height: "100vh",
                width: "100vw",
                bgcolor: "black",
                color: "white",
            }}
        >
            <BackButton PagePath="/"/>
            <Box
                sx={{
                    border: "1px solid white",
                    display: "flex",
                    flexDirection: "column",
                    borderColor: "white",
                    borderWidth: "0.1rem",
                    borderRadius: "1rem",
                    width: "100%",
                    boxSizing: "border-box",
                    alignItems: "center",
                    overflowX: "hidden",
                    marginTop: "10vh",
                }}
            >
                <Box
                    sx={{
                        border: "solid",
                        borderColor: "white",
                        borderWidth: "0.1rem",
                        borderRadius: "01rem",
                        marginBottom: "0.5rem",
                        width: "100%"
                    }}
                >
                    <Typography variant="h6" 
                        sx={{
                            margin: 1,
                            textAlign: "center",
                            fontWeight: "bold"
                        }}
                    >
                        Scans
                    </Typography>
                </Box>
                {scans.map((scan) => {
                    return (
                        <ScanChoice
                            key={scan.scanId}
                            scanId={scan.scanId}
                            startTime={scan.startTime}
                            selected={selectedScan === scan.scanId}
                            onSelect={(scanId: string) => {
                                setSelectedScan(scanId);
                                navigate("/ReportPage")
                            }}
                        />
                    );
                })}
            </Box>
        </Box>
    )
}