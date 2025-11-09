import { Box,Typography, Paper, Table, TableBody,TableCell,TableContainer,TableHead,TableRow, Button} from "@mui/material";
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import Split from "react-split"
import BackButton from "../components/BackButton";

export default function ReportPage({filePath}: {filePath: string | null}) {
    interface Device {
        ipAddress: string;
        hostnames: string | null;
    }
    const [data, setData] = useState<any[]>([]);
    const [devices, setDevices] = useState<Device[]>([]);
    const [selectedDevice, setSelectedDevice] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!filePath) {
            navigate("/")
            return;
        }

        const loadDevices = async () => {
            const deviceList: Device[] = await window.electronAPI.getDevices(filePath);
            setDevices(deviceList);

            if (deviceList.length > 0 && !selectedDevice) {
                setSelectedDevice(deviceList[0].ipAddress);
            }
        };

        loadDevices();
    }, [filePath, selectedDevice, navigate])

    useEffect(() => {
        if (!selectedDevice || !filePath) return;
        
        const loadDeviceData = async () => {
            const rows = await window.electronAPI.getDeviceVulnerabilities(filePath, selectedDevice);
            setData(rows)
        };

        loadDeviceData();
    }, [selectedDevice, filePath]);

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
            <Split
                gutterSize={6}
                sizes={[20, 80]}
                style={{
                    height: "100vh",
                    width: "100vw",
                    paddingTop: "20vh",
                    paddingBottom: 1,
                    display: "flex"
                }}
            >
                <Box
                    sx={{
                        borderRight: "1px solid white",
                        display: "flex",
                        flexDirection: "column"
                    }}
                >
                    <Typography variant="h6" 
                        sx={{
                            marginBottom: 2,
                            textAlign: "center",
                            fontWeight: "bold"
                        }}
                    >
                        Devices
                    </Typography>
                    {devices.map((device) => {
                        let displayName = device.ipAddress
                        if (device.hostnames && device.hostnames !=="[]") {
                            try {
                                const parsed = JSON.parse(device.hostnames);
                                if (Array.isArray(parsed) && parsed.length > 0 && parsed[0].trim() !== "") {
                                    displayName = parsed[0];
                                }
                            } catch {}
                        }
                        return (
                            <Button
                                key={device.ipAddress}
                                variant="outlined"
                                sx={{
                                    borderColor: "white",
                                    borderWidth: "0.1rem",
                                    borderRadius: "0.5rem",
                                    margin: 0.25,
                                    bgcolor: selectedDevice === device.ipAddress ? "gray" : "transparent",
                                    "&:hover": {
                                        bgcolor: "darkgray"
                                    },
                                }}
                                onClick={() => setSelectedDevice(device.ipAddress)}
                            >
                                {displayName}
                            </Button>
                        );
                    })}
                </Box>
                <Box 
                    sx={{
                        display: "flex",
                        flexDirection: "column",
                        bgcolor: "black",
                        color: "white",
                    }}
                >
                    <Typography variant="h5" 
                        sx={{
                            textAlign: "center",
                            fontWeight: "bold"
                        }}
                    >
                        Data from {filePath?.split(/[\\/]/).pop()}
                    </Typography>
                    {!data.length ? (
                        <Box
                            sx={{
                                flex: 1,
                                display: "flex",
                                justifyContent: "center",
                                alignItems: "center"
                            }}
                        >
                            <Typography>No vulnerabiltiies found for this device.</Typography>
                        </Box>
                    ) : (() => {
                        const columns = Object.keys(data[0]);
                        return (
                            <TableContainer component={Paper} sx={{
                                flexGrow: 1,
                                overflowY: "auto",
                            }}>
                                <Table stickyHeader>
                                    <TableHead>
                                        <TableRow>
                                            {columns.map((col) => (
                                                <TableCell key={col} sx={{ fontWeight: "bold"}}>
                                                    {col}
                                                </TableCell>
                                            ))}
                                        </TableRow>
                                    </TableHead>
                                    <TableBody>
                                        {data.map((row, i)=> (
                                            <TableRow key={i}>
                                                {columns.map((col) => (
                                                    <TableCell key={col}>
                                                        {String(row[col])}
                                                    </TableCell>
                                                ))}
                                            </TableRow>
                                        ))}
                                    </TableBody>
                                </Table>
                            </TableContainer>
                        );
                    })()}
                </Box>
            </Split>
        </Box>
    )
}
