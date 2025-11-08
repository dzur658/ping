import { Box, Button, Stack, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function HomePage() {
    const navigate = useNavigate();
    const handleClick = async () => {
        const filePath = await window.electronAPI.openFileDialog();
        if (filePath) {
            console.log("Selected file:", filePath);
        } else {
            console.log("No file selected");
        }
    }

    return (
        <Box 
            sx={{
                height: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                bgcolor: "black",
                color: "white",
            }}
        >
            <Stack spacing={10} alignItems="center" 
                sx={{
                    height: "35vh"
                }}
            >
                <Typography variant="h2" fontWeight="550">
                    Ping
                </Typography>
                <Stack spacing={3}
                    sx={{
                        width: "25vw",
                    }}
                >
                    <Button
                        variant="outlined"
                        onClick={() => navigate("/ScanOptionsPage")}
                    >
                        New Scan
                    </Button>
                    <Button
                        variant="outlined"
                        onClick={handleClick}
                    >
                        Open File
                    </Button>
                </Stack>
            </Stack>
        </Box>
    )
}