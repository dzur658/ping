import {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom'
import {Box, Typography, LinearProgress} from '@mui/material';
import PingLogo from '../../../../resources/PingLogo.svg'

interface ModelProgress {
    percent: number;
    downloaded: number;
    total: number;
}

function formatBytes(bytes: number) {
    if (bytes === 0) return '0 B';
    const gigabytes = bytes / (1024 ** 3);
    if (gigabytes >= 1) return `${gigabytes.toFixed(2)} GB`;
    const megabytes = bytes /(1024 ** 2);
    return `${megabytes.toFixed(1)} MB`;
}

export default function ModelDownloadPage() {
    const navigate = useNavigate();
    const [error, setError] = useState<string | null>(null);
    const [progress, setProgress] = useState<Record<string, ModelProgress>>({
        deviceID: {percent: 0, downloaded: 0, total: 0},
        technicalAssistant: {percent: 0, downloaded: 0, total: 0},
    });

    const labels: Record<string, string> = {
        deviceID: 'Device Identification Model',
        technicalAssistant: 'Technical Assistant Model',
    };

    useEffect(() => {
        const unsubProgress = window.electronAPI.onModelProgress((data) => {
            setProgress(prev => ({
                ...prev,
                [data.modelKey]: {
                    percent: data.percent,
                    downloaded: data.downloaded,
                    total: data.total
                }
            }));
        });

        const unsubComplete = window.electronAPI.onModelDownloadComplete(() => {
            navigate('/');
        })

        const unsubError = window.electronAPI.onModelDownloadError((msg) => {
            setError(msg);
        });

        window.electronAPI.startModelDownload();

        return () => {
            unsubProgress?.();
            unsubComplete?.();
            unsubError?.();
        }
    }, []);

    return (
        <Box
            sx={{
                height: '100vh',
                width: '100vw',
                bgcolor: 'black',
                color: 'white',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                gap: 4,
                padding: 4,
                boxSizing: 'border-box',
            }}
        >
            <Box
                component="img"
                src={PingLogo}
                sx={{
                    filter: 'invert(1)',
                    height: '8vh',
                    width: 'auto',
                    mb: 2
                }}
            />

            <Typography variant="h5" fontWeight="bold">
                Setting up Ping
            </Typography>

            <Typography variant="body1"
                sx={{
                    color: 'white',
                    textAlign: 'center',
                    maxWidth: 480
                }}
            >
                Ping is currently downloading its LLMs which are needed to get started.
                This only happens once and will take a few minutes depending on your internet speed.
            </Typography>

            <Box
                sx={{
                     width: '100%',
                     maxWidth: 480,
                     display: 'flex',
                     flexDirection: 'column',
                     gap: 3
                }}
            >
                {Object.entries(progress).map(([key, value]) => (
                    <Box key={key}>
                        <Box
                            sx={{
                                display: 'flex',
                                justifyContent: 'space-between',
                                mb: 0.5
                            }}
                        >
                            <Typography variant="body2">
                                {labels[key]}
                            </Typography>
                            <Typography variant="body2" sx={{
                                color: "white"
                            }}>
                                {value.percent >= 100
                                    ? 'Completed'
                                    : value.total > 0
                                        ? `${formatBytes(value.downloaded)} / ${formatBytes(value.total)}`
                                        : value.percent > 0 ? `${value.percent}%` : 'Waiting...'
                                }
                            </Typography>
                        </Box>
                        {value.percent > 0 ? (
                            <LinearProgress
                                variant={'determinate'}
                                value={value.percent >= 100 ? 100 : value.percent}
                                sx={{
                                    height: 8,
                                    borderRadius: 4,
                                    backgroundColor: 'rgba(255,255,255,0.1)',
                                    '& .MuiLinearProgress-bar': {
                                        backgroundColor: value.percent >= 100 ? '#4caf50' : '#6cf',
                                        borderRadius: 4,
                                    }
                                }}
                            />
                            ) : (
                                <Box
                                    sx={{
                                        height: 8,
                                        borderRadius: 4,
                                        backgroundColor: 'rgba(255,255,255,0.1)',
                                    }}
                                />
                            )}
                    </Box>
                ))}
            </Box>

            {error && (
                <Box
                    sx={{
                        border: '1px solid red',
                        borderRadius: 2,
                        padding: 2,
                        maxWidth: 480,
                        width: '100%'
                    }}
                >
                    <Typography variant="body2"
                        sx={{
                            color: "error",
                            fontWeight: "bold"
                        }}
                    >
                        Download failed
                    </Typography>

                    <Typography variant="body2"
                        sx={{
                            color: "error",
                        }}
                    >
                        {error}
                    </Typography>

                    <Typography variant="body2"
                        sx={{
                            color: "white",
                            mt: 1
                        }}
                    >
                        Check your internet connection and restart Ping to try again.
                    </Typography>
                </Box>
            )}
        </Box>
    );
}