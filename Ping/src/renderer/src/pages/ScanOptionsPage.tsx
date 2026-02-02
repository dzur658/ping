import { Box, Button, Stack, Typography } from "@mui/material";
import BackButton from "../components/BackButton";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ScanOptionsPage() {
    const navigate = useNavigate();

    const [status, setStatus] = useState<string>("Idle");
    //const [logs, setLogs] = useState<string[]>([]);

    // const appendLog = (msg: string) => {
    //     setLogs(prev => [...prev, msg]);
    // };

    const handleScan = async (scanLocalDevice: boolean) => {
        try {
            const scan  = scanLocalDevice
                ? await window.electronAPI.scanLocalDevice()
                : await window.electronAPI.scanLocalNetwork();
            
            console.log(scan)
            
            const xmlPath = await window.electronAPI.startScan(scan);

            const newScanId = await window.electronAPI.processScan(xmlPath);

            navigate("/ReportPage", { state: {scanId: newScanId, filePath: await window.electronAPI.getDBPath()}});
        } catch (err) {
            console.error("Scan failed:", err);
        }
    }

    useEffect(() => {
        const unsubStatus = window.electronAPI.onNmapStatus((s) => setStatus(s.message));
        const unsubScan = window.electronAPI.onProcessScanStatus((s) => setStatus(s.message));
        //const unsubLog = window.electronAPI.onLog(appendLog);

        return () => {
            unsubStatus?.();
            unsubScan?.();
            //unsubLog?.();
        };
    }, []);

    return (
        <Box 
            sx={{
                height: "100vh",
                width: "100vw",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                bgcolor: "black",
                color: "white",
            }}
        >
            <BackButton PagePath="/"/>
            <Stack spacing={10} alignItems="center" 
                sx={{
                    height: "35vh"
                }}
            >
                <Typography variant="h2" fontWeight="550">
                    What should I scan?
                </Typography>
                
                <Typography variant="body1">
                    Status: {status}
                </Typography>

                <Stack spacing={3}
                    sx={{
                        width: "25vw",
                    }}
                >
                    <Button
                        variant="outlined"
                        onClick={async () => {
                            handleScan(false)
                        }}
                    >
                        My whole network
                    </Button>
                    <Button
                        variant="outlined"
                        onClick={async () => {
                            handleScan(true)
                        }}
                    >
                        Just this device
                    </Button>
                </Stack>
            </Stack>
        </Box>
    )
}