import { Box,Typography, Paper, Table, TableBody,TableCell,TableContainer,TableHead,TableRow, Button,} from "@mui/material";
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import Split from "react-split"
import BackButton from "../components/BackButton";
import DeviceMenu from "../components/DeviceMenu";

interface ReportPageProps {
  filePath: string | null;
  selectedScan: string | null;
}

export default function ReportPage({filePath,selectedScan}: ReportPageProps) {
    interface Device {
        ipAddress: string;
        hostnames: string | null;
    }
    const [data, setData] = useState<any[]>([]);
    const [devices, setDevices] = useState<Device[]>([]);
    const [selectedDevice, setSelectedDevice] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!filePath || !selectedScan) {
            navigate("/")
            return;
        }

        const loadDevices = async () => {
            const deviceList: Device[] = await window.electronAPI.getDevices(filePath, selectedScan);
            setDevices(deviceList);

            if (deviceList.length > 0 && !selectedDevice) {
                setSelectedDevice(deviceList[0].ipAddress);
            }
        };

        loadDevices();
    }, [filePath, selectedScan, selectedDevice, navigate])

    useEffect(() => {
        if (!selectedDevice || !filePath) return;
        
        const loadDeviceData = async () => {
            const rows = await window.electronAPI.getDeviceVulnerabilities(filePath, selectedDevice);
            setData(rows)
        };

        loadDeviceData();
    }, [selectedDevice, filePath]);

    const selectedDeviceName = devices.find(device => device.ipAddress === selectedDevice)?.hostnames
        ? (() => {
            try {
                const parsed = JSON.parse(devices.find(device => device.ipAddress === selectedDevice)?.hostnames || "[]");
                return Array.isArray(parsed) && parsed.length > 0 && parsed[0].trim() !== ""
                    ? parsed[0]
                    : selectedDevice
            } catch {
                return selectedDevice;
            }
        })()
        : selectedDevice

    const vulnerabilityCount = data.length

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
            <BackButton PagePath="/ScanSelectionPage"/>
            <Split
                gutterSize={6}
                sizes={[20, 60, 20]}
                style={{
                    height: "100vh",
                    width: "100vw",
                    paddingBottom: 1,
                    display: "flex"
                }}
            >
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
                            Devices
                        </Typography>
                    </Box>
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
                            <DeviceMenu 
                                key={device.ipAddress}
                                displayName={displayName}
                                ipAddress={device.ipAddress}
                                selected={selectedDevice === device.ipAddress}
                                onSelect={setSelectedDevice}
                            />
                        );
                    })}
                </Box>
                <Box 
                    sx={{
                        position: "relative",
                        display: "flex",
                        flexDirection: "column",
                        bgcolor: "black",
                        color: "white",
                        width: "100%",
                        height: "100%"
                    }}
                >
                    <Typography
                        variant="h3"
                        sx={{
                            position: "absolute",
                            top: "1vh",
                            alignSelf: "center",
                            textAlign: "center"
                        }}
                    >
                        {filePath?.split(/[\\/]/).pop()}
                    </Typography>

                    <Typography
                        variant="h4"
                        sx={{
                            position: "absolute",
                            top: "11vh",
                            marginLeft: 5,
                            alignSelf: "flex-start",
                            textAlign: "center",
                            paddingBottom: "0.2rem",
                            borderBottom: "solid",
                            borderWidth: "1px"
                        }}
                    >
                        {selectedDeviceName}
                    </Typography>

                    <Typography
                        variant="subtitle1"
                        sx={{
                            position: "absolute",
                            top: "16.3vh",
                            marginLeft: 6,
                            alignSelf: "flex-start",
                            textAlign: "center",
                        }}
                    >
                        Vulnerability Count: {vulnerabilityCount}
                    </Typography>

                    {!data.length ? (
                        <Box
                            sx={{
                                flex: 1,
                                display: "flex",
                                justifyContent: "center",
                                alignItems: "center",
                            }}
                        >
                            <Typography>No vulnerabiltiies found for this device.</Typography>
                        </Box>
                    ) : (() => {
                        const columns = Object.keys(data[0]);
                        return (
                            <TableContainer 
                            component={Paper} 
                            sx={{
                                marginTop: "20vh",
                                flexGrow: 1,
                                overflowY: "auto",
                                "&::-webkit-scrollbar": {
                                    width: "8px",
                                },
                                "&::-webkit-scrollbar-track": {
                                    background: "rgba(255,255,255,0.05)", // very subtle track
                                    borderRadius: "4px",
                                },
                                "&::-webkit-scrollbar-thumb": {
                                    backgroundColor: "rgba(255,255,255,0.3)", // hidden by default
                                    borderRadius: "4px",
                                    transition: "background-color 0.3s",
                                },
                                "&:hover::-webkit-scrollbar-thumb": {
                                    backgroundColor: "rgba(255,255,255,0.2)", // visible on hover
                                },
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
                        marginTop: "20vh"
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
                            Ask Ping
                        </Typography>
                    </Box>
                </Box>
            </Split>
        </Box>
    )
}
