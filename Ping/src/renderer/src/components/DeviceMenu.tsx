import {Typography,Button,Menu,MenuItem,} from "@mui/material";
import { MoreHoriz, } from "@mui/icons-material";
import WarningAmberIcon from '@mui/icons-material/WarningAmber';
import { useState } from "react";

export default function DeviceMenu ({displayName, ipAddress, selected, onSelect, showAlert}) {
    const [anchorElement, setAnchorElement] = useState<null | HTMLElement>(null);
    const handleMenuOpen = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.stopPropagation();
        setAnchorElement(event.currentTarget);
    };

    const handleMenuClose = () => setAnchorElement(null)

    return (
        <Button
            variant="outlined"
            endIcon={
                <span
                    onClick={handleMenuOpen}
                    style={{
                        color: "white",
                        padding: 0.5,
                    }}
                >
                    <MoreHoriz />
                </span>
            }
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
                width: "90%",
            }}
            onClick={() => onSelect(ipAddress)}
        >
            <Typography 
                sx={{
                    fontSize: "small"
                }}
            >
                {displayName}
            </Typography>

            <Menu
                anchorEl={anchorElement}
                open={Boolean(anchorElement)}
                onClose={handleMenuClose}
            >
                <MenuItem onClick={() => alert(`View ${ipAddress}`)}>View</MenuItem>
                <MenuItem onClick={() => alert(`Detals for ${ipAddress}`)}>
                    Details
                </MenuItem>
            </Menu>
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