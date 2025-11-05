import { Box, Button, Stack, Typography } from "@mui/material";

export default function HomePage() {
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
                        onClick={() => console.log("New Scan")}
                    >
                        New Scan
                    </Button>
                    <Button
                        variant="outlined"
                        onClick={() => console.log("Open File")}
                    >
                        Open File
                    </Button>
                </Stack>
            </Stack>
        </Box>
    )
}