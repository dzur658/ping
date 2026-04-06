import {Box} from "@mui/material";
import MarkdownRenderer from "@renderer/components/MarkdownRenderer";

interface RecommendationChoiceProps {
    interType: string;
    content: string | null;
}

export default function RecommendationChoice ({content}: RecommendationChoiceProps) {
    if (!content) return null
    return (
        <Box
            sx={{
                padding: "1rem",
                userSelect: "text",
                cursor: "text",
            }}
        >
            <MarkdownRenderer content={content}/>
        </Box>
    );
}