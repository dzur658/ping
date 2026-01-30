import { Box, Button, Stack, Typography } from "@mui/material";
import BackButton from "../components/BackButton";

export default function HomePage() {
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
                <Stack spacing={3}
                    sx={{
                        width: "25vw",
                    }}
                >
                    <Button
                        variant="outlined"
                        onClick={async () => {
                            const scan = await window.electronAPI.scanLocalNetwork();
                            console.log("Network scan:", scan);

                            const xmlPath = await window.electronAPI.runScan(scan.args)
                            console.log("Nmap XML written to:", xmlPath);

                            const pythonOut = await window.electronAPI.processScan(xmlPath)
                            console.log("python out:", pythonOut)
                        }}
                    >
                        My whole network
                    </Button>
                    <Button
                        variant="outlined"
                        onClick={async () => {
                            const scan = await window.electronAPI.scanLocalDevice();
                            console.log("Device scan:", scan)

                            const xmlPath = await window.electronAPI.runScan(scan.args)
                            console.log("Nmap XML written to:", xmlPath);

                            const pythonOut = await window.electronAPI.processScan(xmlPath)
                            console.log("python out:", pythonOut)
                        }}
                    >
                        Just this device
                    </Button>
                </Stack>
            </Stack>
        </Box>
    )
}