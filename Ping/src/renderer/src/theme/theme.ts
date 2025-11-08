import { createTheme, Theme } from "@mui/material/styles";

const theme: Theme = createTheme({
    palette: { mode: "dark" },
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    color: "white",
                    borderColor: "white",
                    "&:hover": {
                        borderColor: "gray",
                    },
                },
            },
            variants: [
                {
                    props: {
                        variant: "outlined"
                    },
                    style: {
                        fontSize: "1rem",
                        fontWeight: "normal",
                        color: "white",
                        borderColor: "white",
                        borderWidth: "0.3rem",
                        borderRadius: "0.5rem",
                        "&:hover": {
                            borderColor: "gray",
                        },
                    },
                },
            ],
        },
    },
});

export default theme;