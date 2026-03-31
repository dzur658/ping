import {Box} from "@mui/material";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import 'github-markdown-css'

interface MarkdownRendererProps {
    content: string | null;
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
    const normalized = content
        ?.replace(/^(\s*[-*+\d.]+\s.+)\n\n(?=\s*[-*+\d.]+\s)/gm, '$1\n')
        ?? '';
    return (
        <Box
            className="markdown-body"
            sx={{
                width: "100%",
                backgroundColor: "transparent !important",
                color: "inherit !important",
                fontSize: "1rem !important",
                "& h1, & h2, & h3": { marginTop: "0.8rem !important", marginBottom: "0.3rem !important" },
                "& p": { marginTop: "0.5rem !important", marginBottom: "0.5rem !important" },
                "& ul, & ol": { marginTop: "0.2rem !important", marginBottom: "0.2rem !important", paddingLeft: "1.5rem !important" },
                "& li": { marginBottom: "0.1rem !important" },
                "& li + li": { marginTop: "0 !important" },
            }}
        >
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
            >
                {normalized}
            </ReactMarkdown>
        </Box>
    )
}

