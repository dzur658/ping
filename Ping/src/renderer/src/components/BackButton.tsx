import {Box, Button} from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import {useNavigate} from "react-router-dom";

interface BackButtonProperties {
    PagePath?: string;
}

export default function BackButton({PagePath}: BackButtonProperties) {
    const navigate = useNavigate();
    const handleClick = () => {
        if (PagePath) navigate(PagePath);
        else navigate(-1);
    }
    return (
        <Box 
            sx={{
                bgcolor: "black",
                color: "white",
                position: "absolute",
                zIndex: 1000,
            }}
        >
            <Button
                startIcon={<ArrowBackIcon />}
                sx={{
                    position: "fixed",
                    top: "1rem",
                    left: "1rem"
                }}
                onClick={handleClick}
            >
                Back
            </Button>
        </Box>
    )
}
