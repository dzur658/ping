import {IconButton,Menu,MenuItem,TableRow,TableCell,} from "@mui/material";
import { MoreHoriz } from "@mui/icons-material";
import { useState } from "react";

export default function ScanChoice ({scanId, startTime, onSelect}) {
    const [anchorElement, setAnchorElement] = useState<null | HTMLElement>(null);
    const [menuOpen, setMenuOpen] = useState(false);

    const handleMenuOpen = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.stopPropagation();
        setMenuOpen(true);
        setAnchorElement(event.currentTarget);
    };

    const handleMenuClose = () => {
        setMenuOpen(false);
        setAnchorElement(null)
    }

    return (
        <TableRow
            hover
            onClick={() => {
                if (menuOpen) return;
                onSelect(scanId);
            }}
            sx={{
                cursor: "pointer",
                "&:hover": {
                    backgroundColor: "rgba(255,255,255,0.08"
                }
            }}
        >
            <TableCell 
                sx={{
                    color: "white"
                }}
            >
                {scanId}
            </TableCell>
            <TableCell 
                sx={{
                    color: "white"
                }}
            >
                {startTime || "Unknown"}
            </TableCell>
            <TableCell
                align="right"
            >
                <IconButton
                    onClick={handleMenuOpen}
                    sx={{
                        color: "white"
                    }}
                >
                    <MoreHoriz />
                </IconButton>

                <Menu
                    anchorEl={anchorElement} open={Boolean(anchorElement)} onClose={handleMenuClose}
                >
                    <MenuItem
                        onClick={(event) => {
                            event.stopPropagation();
                            alert(`Details ${scanId}`)
                            handleMenuClose();
                        }}
                    >
                        Details
                    </MenuItem>
                    <MenuItem
                        onClick={(event) => {
                            event.stopPropagation();
                            alert(`Delete ${scanId}`)
                            handleMenuClose();
                        }}
                    >
                        Delete
                    </MenuItem>
                </Menu>
            </TableCell>
        </TableRow>
    );
}