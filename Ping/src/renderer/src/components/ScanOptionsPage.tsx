import { Box, Button, Stack, Typography } from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { useNavigate } from "react-router-dom";

export default function HomePage() {
    const navigate = useNavigate();

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
            <Button
                startIcon={<ArrowBackIcon />}
                sx={{
                    position: "fixed",
                    top: "1rem",
                    left: "1rem"
                }}
                onClick={() => navigate("/")}
            >
                Back
            </Button>
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
                        onClick={() => console.log("New Scan")}
                    >
                        My whole network
                    </Button>
                    <Button
                        variant="outlined"
                        onClick={() => console.log("Open File")}
                    >
                        Just this device
                    </Button>
                </Stack>
            </Stack>
        </Box>
    )
}