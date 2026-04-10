# Ping - Developer Guide

This document covers everything needed to work on the Ping Electron application. For a user-facing overview of what Ping does, see the [root README](../README.md).

---

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) with the following extensions:
  - [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
  - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
  - [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

A `.vscode/extensions.json` file is included; VSCode will prompt you to install recommended extensions automatically.

---

## Project Setup

All commands below are run from the `Ping/` directory.

### Install dependencies

```bash
npm install
```

`postinstall` runs `electron-builder install-app-deps` automatically to build native modules (including `better-sqlite3`) against the bundled Electron version.

### Development

```bash
npm run dev
```

Starts the Electron process and the Vite dev server with HMR. The renderer reloads on file changes; the main process requires a restart.

### Preview a production build

```bash
npm start
```

Runs `electron-vite preview` against the last compiled output in `out/`.

---

## Available Scripts

| Script | Command | Description |
|---|---|---|
| `dev` | `electron-vite dev` | Start in development mode with HMR |
| `start` | `electron-vite preview` | Preview the last production build |
| `build` | `npm run typecheck && electron-vite build` | Full typecheck + compile |
| `build:win` | `build + electron-builder --win` | Windows NSIS installer |
| `build:mac` | `electron-vite build + electron-builder --mac` | macOS dmg (no typecheck gate) |
| `build:linux` | `electron-vite build + electron-builder --linux` | Linux AppImage / deb / snap |
| `build:unpack` | `build + electron-builder --dir` | Unpacked directory (useful for testing) |
| `typecheck` | runs both typecheck scripts | Full TypeScript check across all tsconfigs |
| `typecheck:node` | `tsc --noEmit -p tsconfig.node.json` | Type-check main + preload only |
| `typecheck:web` | `tsc --noEmit -p tsconfig.web.json` | Type-check renderer only |
| `lint` | `eslint --cache .` | Lint all source files |
| `format` | `prettier --write .` | Auto-format all files |
| `rebuild` | `electron-rebuild -f -w better-sqlite3` | Rebuild native modules for current Electron version |

---

## TypeScript Configuration

The project uses **TypeScript project references** to keep the three Electron contexts isolated:

| Config file | Covers | Key settings |
|---|---|---|
| `tsconfig.json` | Root, references node + web | Project references only |
| `tsconfig.node.json` | `src/main/`, `src/preload/`, `electron.vite.config.ts` | Node target, CommonJS, `@electron-toolkit/tsconfig/tsconfig.node.json` base |
| `tsconfig.web.json` | `src/renderer/` | DOM target, `@renderer/*` path alias, `@electron-toolkit/tsconfig/tsconfig.web.json` base |

The `@renderer/*` alias resolves to `src/renderer/src/` and is set up in both `tsconfig.web.json` and `electron.vite.config.ts`.

---

## IPC Channel Reference

Communication between the renderer and the main process goes through `window.electronAPI` (defined in `src/preload/index.ts`).

### Invoke channels (renderer → main, returns a Promise)

| Channel | Preload method | Description |
|---|---|---|
| `models:checkStatus` | `checkModelStatus()` | Returns `{ deviceIDReady, technicalAssistantReady }` |
| `models:startDownload` | `startModelDownload()` | Begins streaming download of both GGUF models |
| `database:getPath` | `getDBPath()` | Returns the user-data path to `networkscans.db` |
| `dialog:openSQLiteFile` | `openSQLiteFile()` | Opens a file-picker dialog; returns selected `.sqlite` path |
| `sqlite:getScans` | `getScans(filePath)` | Returns all scan rows from the given DB path |
| `sqlite:getScanStartTime` | `getScanStartTime(filePath, scanId)` | Returns ISO timestamp for a scan |
| `sqlite:getDevices` | `getDevices(filePath, scanId)` | Returns device rows for a scan |
| `sqlite:getDeviceRecommendations` | `getDeviceRecommendations(filePath, deviceId)` | Returns security guidance from the knowledge base |
| `nmap:startScan` | `startScan(range)` | Runs Nmap; returns path to the output XML |
| `nmap:scanLocalDevice` | `scanLocalDevice()` | Returns the host's IPv4 address |
| `nmap:scanLocalNetwork` | `scanLocalNetwork()` | Returns the local subnet CIDR (e.g. `192.168.1.0/24`) |
| `python:processScan` | `processScan(xmlPath)` | Runs `orchestrator.exe`; returns the new `scanId` |
| `llama:analyzeScanDevices` | `analyzeScanDevices(scanId)` | Runs device-identification model over all devices in a scan |
| `llama:askFollowup` | `askFollowup(scanId, deviceId, message, history)` | Chat with device-ID model to clarify ambiguous devices |
| `llama:askPing` | `askPing(deviceId, message, history)` | Chat with technical-assistant model for a known device |

### Push channels (main → renderer, one-way events)

| Channel | Preload subscription | Payload | Description |
|---|---|---|---|
| `models:progress` | `onModelProgress(cb)` | `{ modelKey, loaded, total, percent }` | Download progress per model |
| `models:downloadComplete` | `onModelDownloadComplete(cb)` | `{ modelKey }` | Model file fully written |
| `models:downloadError` | `onModelDownloadError(cb)` | `{ modelKey, error }` | Download failure |
| `nmap:status` | `onNmapStatus(cb)` | `string` | Nmap lifecycle status messages |
| `nmap:log` | `onLog(cb)` | `string` | Raw Nmap stdout lines |
| `scan:status` | `onProcessScanStatus(cb)` | `string` | Orchestrator lifecycle messages |
| `db:refresh` | `onRefreshData(cb)` | (none) | Tells the renderer to reload device data (fired after follow-up identification) |

---

## Native Modules

`better-sqlite3` is a native Node.js addon. It must be compiled against the exact Electron version in use. This happens automatically on `npm install` via `postinstall`, but if you upgrade Electron or switch Node versions, run:

```bash
npm run rebuild
```

---

## Background Processes

The main process manages three external executables:

| Process | Source | Spawned by | Notes |
|---|---|---|---|
| **Nmap** | System install | `nmap:startScan` | Windows default path hardcoded; falls back to `nmap` on `PATH` |
| **`orchestrator.exe`** | `resources/python/` | `python:processScan` | Bundled; accepts `--xml-file`, `--json-file`, `--db-file` args |
| **`llama-server`** | `resources/llama-cpp-gpu/` or `llama-cpp-cpu/` | `switchModel()` | Runs on port **3500**; killed and restarted when switching between models |

GPU detection uses `wmic path win32_VideoController get name` (Windows only). NVIDIA/AMD cards use the GPU binary; all others fall back to CPU.

---

## Windows-Only Considerations

The current build targets **Windows** as the primary platform:

- `llama-server.exe` and `orchestrator.exe` are Windows executables.
- GPU detection relies on `wmic`, which is not available on macOS or Linux.
- Nmap's default path is hardcoded for the Windows installer location.

macOS and Linux build targets (`build:mac`, `build:linux`) exist in `package.json` and `electron-builder.yml` but require platform-specific binaries to be placed in `resources/` before they will function correctly.
