import { Box,Typography, Table, TableBody,TableContainer,} from "@mui/material";
import { useEffect, useState } from 'react';
import { useNavigate, useLocation } from "react-router-dom";
import Split from "react-split"
import BackButton from "@renderer/components/BackButton";
import DeviceMenu from "@renderer/components/DeviceMenu";
import RecommendationChoice from "@renderer/components/RecommendationChoice";

interface ReportPageProps {
  filePath: string | null;
  selectedScan: string | null;
  //setSelectedRecommendation: (scanId: string | null) => void;
}

export default function ReportPage({filePath, selectedScan,}: ReportPageProps) {
    const location  = useLocation();
    const scanIdEffective = location.state?.scanId ?? selectedScan;
    const filePathEffective = location.state?.filePath ?? filePath;

    const [chatMessages, setChatMessages] = useState<
    { role: "user" | "assistant"; content: string }[]
    >([]);

    const [chatInput, setChatInput] = useState("");
    const [chatLoading, setChatLoading] = useState(false);

    async function sendAskPing() {
        if (!chatInput.trim() || chatLoading) return;

        const userMessage = chatInput;

        setChatMessages(prev => [
            ...prev,
            { role: "user", content: userMessage }
        ]);

        setChatInput("");
        setChatLoading(true);

        try {
            const reply = await window.electronAPI.askPing(userMessage);

            setChatMessages(prev => [
            ...prev,
            { role: "assistant", content: reply }
            ]);
        } catch (err) {
            setChatMessages(prev => [
            ...prev,
            {
                role: "assistant",
                content: "Ping ran into an error."
            }
            ]);
        } finally {
            setChatLoading(false);
        }
    }

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
    const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
    const [expandedRecommendation, setExpandedRecommendation] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!filePathEffective || !scanIdEffective) {
            navigate("/")
            return;
        }

        const loadDevices = async () => {
            const deviceList: Device[] = await window.electronAPI.getDevices(filePathEffective, scanIdEffective);
            setDevices(deviceList);

            if (deviceList.length > 0 && !selectedDevice) {
                setSelectedDevice(deviceList[0].ipAddress);
            }
        };

        loadDevices();
    }, [filePathEffective, scanIdEffective, selectedDevice, navigate])

    useEffect(() => {
        if (!filePathEffective) {
            navigate("/")
            return;
        }

        const loadScans = async () => {
            if (!selectedDevice || !filePathEffective) return;
            const recommendationList: Recommendation[] = await window.electronAPI.getDeviceRecommendations(filePathEffective, selectedDevice);
            setRecommendations(recommendationList);
        };

        loadScans();
    }, [filePathEffective, selectedDevice, navigate])

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
                        {filePathEffective?.split(/[\\/]/).pop()}
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

                    {recommendations.length === 0 ? (
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
                    ) : (
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
                                    marginTop: "20vh",
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
                                        Recommendations
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
                                        {/* <TableHead>
                                            <TableRow>
                                                <TableCell
                                                    sx={{
                                                        color: "white",
                                                        fontWeight: "bold"
                                                    }}
                                                >
                                                    Description
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
                                            </TableRow>
                                        </TableHead> */}
                                        <TableBody>
                                            {recommendations.map((recommendation) => {
                                                return (
                                                    <RecommendationChoice
                                                        key={recommendation.interType}
                                                        interType={recommendation.interType}
                                                        content={recommendation.content ?? ""}
                                                        expanded={expandedRecommendation === recommendation.interType}
                                                        onSelect={() =>setExpandedRecommendation(
                                                            expandedRecommendation === recommendation.interType ? null : recommendation.interType)
                                                        }
                                                    />
                                                );
                                            })}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Box>
                    )}
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
                    {/* <Box
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
                    </Box> */}
                    <Box
                        sx={{
                            flex: 1,
                            width: "100%",
                            display: "flex",
                            flexDirection: "column",
                            padding: 1
                        }}
                        >
                        {/* Chat history */}
                        <Box
                            sx={{
                            flex: 1,
                            overflowY: "auto",
                            mb: 1,
                            pr: 1
                            }}
                        >
                            {chatMessages.map((msg, idx) => (
                            <Typography
                                key={idx}
                                sx={{
                                color: msg.role === "assistant" ? "#6cf" : "white",
                                mb: 1,
                                whiteSpace: "pre-wrap"
                                }}
                            >
                                <strong>{msg.role === "assistant" ? "Ping" : "You"}:</strong>{" "}
                                {msg.content}
                            </Typography>
                            ))}

                            {chatLoading && (
                            <Typography sx={{ color: "#5f5f5f" }}>
                                Ping is thinking…
                            </Typography>
                            )}
                        </Box>

                        {/* Input */}
                        <Box sx={{ display: "flex", gap: 1 }}>
                            <input
                            value={chatInput}
                            onChange={e => setChatInput(e.target.value)}
                            onKeyDown={e => e.key === "Enter" && sendAskPing()}
                            style={{
                                flex: 1,
                                background: "black",
                                color: "white",
                                border: "1px solid white",
                                borderRadius: "6px",
                                padding: "6px"
                            }}
                            placeholder="Ask Ping about this device…"
                            />
                        </Box>
                        </Box>
                </Box>
            </Split>
        </Box>
    )
}
