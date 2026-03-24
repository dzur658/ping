import { Box,Typography,TableContainer,Table,TableHead,TableBody,TableRow,TableCell} from "@mui/material";
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
    //const [selectedScan, setLocalSelectedScan] = useState<string | null>(null);
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
                                <TableRow>
                                    <TableCell
                                        sx={{
                                            color: "white",
                                            fontWeight: "bold"
                                        }}
                                    >
                                        Scan ID
                                    </TableCell>
                                    <TableCell
                                        sx={{
                                            color: "white",
                                            fontWeight: "bold"
                                        }}
                                    >
                                        Start Time
                                    </TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {scans.map((scan) => {
                                    return (
                                        <ScanChoice
                                            key={scan.scanId}
                                            scanId={scan.scanId}
                                            startTime={scan.startTime}
                                            onSelect={(scanId: string) => {
                                                setSelectedScan(scanId);
                                                navigate("/ReportPage")
                                            }}
                                        />
                                    );
                                })}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </Box>
            </Box>
        </Box>
    )
}