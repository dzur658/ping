import {IconButton,Menu,MenuItem,TableRow,TableCell,Box,} from "@mui/material";
import { MoreHoriz } from "@mui/icons-material";
import { useState } from "react";
import MarkdownRenderer from "@renderer/components/MarkdownRenderer";

interface RecommendationChoiceProps {
    interType: string;
    content: string;
    expanded: boolean;
    onSelect: () => void;
}

export default function RecommendationChoice ({interType, content, expanded, onSelect}: RecommendationChoiceProps) {
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
                onSelect();
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
                {interType}
            </TableCell>
            <TableCell 
                sx={{
                    color: "white"
                }}
            >
                <Box
                    sx={{
                        overflow: "hidden",
                        display: "-webkit-box",
                        WebkitBoxOrient: "vertical",
                        WebkitLineClamp: expanded ? "none" : 2,
                    }}
                >
                    <MarkdownRenderer content={content} />
                </Box>
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
                            alert(`Details ${interType}`)
                            handleMenuClose();
                        }}
                    >
                        Details
                    </MenuItem>
                    <MenuItem
                        onClick={(event) => {
                            event.stopPropagation();
                            alert(`Delete ${interType}`)
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