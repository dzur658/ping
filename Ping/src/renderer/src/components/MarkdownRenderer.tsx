import {Box} from "@mui/material";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import 'github-markdown-css'

interface MarkdownRendererProps {
    content: string | null;
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
    return (
        <Box
            sx={{
                width: "100%"
            }}
        >
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
            >
                {content}
            </ReactMarkdown>
        </Box>
    )
}

