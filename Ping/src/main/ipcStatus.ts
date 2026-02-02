import {BrowserWindow} from "electron";

export function sendStatus(channel: string, payload: unknown) {
    for (const win of BrowserWindow.getAllWindows()) {
        if (!win.isDestroyed()) {
            win.webContents.send(channel, payload);
        }
    }
}
