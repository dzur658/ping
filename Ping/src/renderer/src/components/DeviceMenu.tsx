import {Typography,Button,} from "@mui/material";
import WarningAmberIcon from '@mui/icons-material/WarningAmber';

export default function DeviceMenu ({displayName, ipAddress, selected, onSelect, showAlert}) {
    return (
        <Button
            variant="outlined"
            sx={{
                borderColor: "white",
                borderWidth: "0.1rem",
                borderRadius: "1rem",
                margin: 0.5,
                bgcolor: selected ? "gray" : "transparent",
                "&:hover": {
                    bgcolor: "darkgray"
                },
                textTransform: "none",
                justifyContent: "space-between",
                color: "white",
                width: "95%",
            }}
            onClick={() => onSelect(ipAddress)}
        >
            <Typography 
                sx={{
                    fontSize: "medium"
                }}
            >
                {displayName}
            </Typography>
            {showAlert && (
                <WarningAmberIcon
                    sx={{
                        color: "#ffcc00"
                    }}
                />
            )}
        </Button>
    );
}