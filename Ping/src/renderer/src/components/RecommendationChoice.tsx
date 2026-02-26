import {TableRow,TableCell,Box,} from "@mui/material";
import MarkdownRenderer from "@renderer/components/MarkdownRenderer";

interface RecommendationChoiceProps {
    interType: string;
    content: string | null;
    expanded: boolean;
    onSelect: () => void;
}

export default function RecommendationChoice ({content, expanded, onSelect}: RecommendationChoiceProps) {
    return (
        <TableRow
            hover
            onClick={() => {
                onSelect();
            }}
            sx={{
                cursor: "pointer",
                "&:hover": {
                    backgroundColor: "rgba(255,255,255,0.08"
                }
            }}
        >
            {/* <TableCell 
                sx={{
                    color: "white"
                }}
            >
                {interType}
            </TableCell> */}
            <TableCell 
                sx={{
                    color: "white"
                }}
            >
                <Box className="markdown-body"
                    sx={{
                        overflow: "hidden",
                        display: "-webkit-box",
                        WebkitBoxOrient: "vertical",
                        WebkitLineClamp: expanded ? 2 : "none",
                        backgroundColor: "transparent"
                    }}
                >
                    <MarkdownRenderer content={content} />
                </Box>
            </TableCell>
            {/* <TableCell
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
            </TableCell> */}
        </TableRow>
    );
}