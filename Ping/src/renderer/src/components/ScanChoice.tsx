import {TableRow,TableCell,} from "@mui/material";

export default function ScanChoice ({scanId, startTime, onSelect}) {
    return (
        <TableRow
            hover
            onClick={() => {
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
        </TableRow>
    );
}