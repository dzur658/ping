import { Box,Typography, Paper, Table, TableBody,TableCell,TableContainer,TableHead,TableRow,} from "@mui/material";
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import Split from "react-split"
import BackButton from "../components/BackButton";
import DeviceMenu from "../components/DeviceMenu";
// import React from 'react';
// import ReactMarkdown from 'react-markdown';
// import remarkGfm from 'remark-gfm';
import RecommendationChoice from "@renderer/components/RecommendationChoice";

interface ReportPageProps {
  filePath: string | null;
  selectedScan: string | null;
  setSelectedRecommendation: (scanId: string | null) => void;
}

export default function ReportPage({filePath, selectedScan, setSelectedRecommendation}: ReportPageProps) {
    interface Device {
        ipAddress: string;
        hostnames: string | null;
    }

    interface Recommendation {
        interType: string;
        content: string | null;
    }

    //const [data, setData] = useState<any[]>([]);
    const [devices, setDevices] = useState<Device[]>([]);
    const [selectedDevice, setSelectedDevice] = useState<string | null>(null);
    const [recommendations, setRecommendation] = useState<Recommendation[]>([]);
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

    // useEffect(() => {
    //     if (!selectedDevice || !filePath) return;
        
    //     const loadDeviceData = async () => {
    //         const rows = await window.electronAPI.getDeviceRecommendations(filePath, selectedDevice);
    //         setData(rows)
    //     };

    //     loadDeviceData();
    // }, [selectedDevice, filePath]);

    useEffect(() => {
        if (!filePath) {
            navigate("/")
            return;
        }

        const loadScans = async () => {
            if (!selectedDevice || !filePath) return;
            const recommendationList: Recommendation[] = await window.electronAPI.getDeviceRecommendations(filePath, selectedDevice);
            setRecommendation(recommendationList);

            if (recommendationList.length <= 0) {
                navigate("/")
                return;
            }
        };

        loadScans();
    }, [filePath, navigate])

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

    const recommendationCount = recommendations.length

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
                        Recommendation Count: {recommendationCount}
                    </Typography>

                    {!recommendations.length ? (
                        <Box
                            sx={{
                                flex: 1,
                                display: "flex",
                                justifyContent: "center",
                                alignItems: "center",
                            }}
                        >
                            <Typography>No recommendations found for this device.</Typography>
                        </Box>
                    ) : (() => {
                        return (
                            <Box
                                sx={{
                                    border: "1px solid white",
                                    display: "flex",
                                    flexDirection: "column",
                                    borderColor: "white",
                                    borderWidth: "0.1rem",
                                    borderRadius: "1rem",
                                    width: "100%",
                                    height: "100%",
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
                                <TableContainer
                                    sx={{
                                        width: "100%",
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
                                    }}
                                >
                                    <Table>
                                        <TableHead>
                                            <TableCell
                                                sx={{
                                                    color: "white",
                                                    fontWeight: "bold"
                                                }}
                                            >
                                                Recommendation Type
                                            </TableCell>
                                            <TableCell
                                                sx={{
                                                    color: "white",
                                                    fontWeight: "bold"
                                                }}
                                            >
                                                Recommendation
                                            </TableCell>
                                            <TableCell
                                                sx={{
                                                    color: "white",
                                                    align: "right",
                                                    fontWeight: "bold"
                                                }}
                                            >
                                            </TableCell>
                                        </TableHead>
                                        <TableBody>
                                            {recommendations.map((recommendation) => {
                                                return (
                                                    <RecommendationChoice
                                                        key={recommendation.interType}
                                                        interType={recommendation.interType}
                                                        content={recommendation.content}
                                                        onSelect={(interType: string) => {
                                                            setSelectedRecommendation(interType);
                                                            navigate("/ReportPage")
                                                        }}
                                                    />
                                                );
                                            })}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Box>
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
