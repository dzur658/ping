import './assets/main.css'
import { ThemeProvider } from "@mui/material/styles";
import Theme from "./theme/theme";
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

createRoot(document.getElementById('root')!).render(
  <ThemeProvider theme={Theme}>
    <StrictMode>
      <App />
    </StrictMode>
  </ThemeProvider>
)
