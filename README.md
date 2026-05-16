# Fast Math Trainer - Multi-Platform

A comprehensive mental math training application supporting Trachtenberg and Vedic methods.

## Project Structure

- `web-app/`: The core web application built with React and Vite.
- `windows-app/`: Windows desktop application using Electron.
- `android-app/`: Android mobile application using Capacitor.

## Features

- **Trachtenberg System**: Multiplication by 11, 12, 5, and Rapid Addition.
- **Vedic Mathematics**: Squaring (ending in 5, general method), Square Root (perfect squares), and Complementary Addition.
- **Multi-platform support**: Native-like experience on Web, Desktop, and Mobile.

## Getting Started

Each application resides in its own folder and has its own `package.json`. Navigate to the desired folder to run platform-specific commands.

### Web App

```bash
cd web-app
npm install
npm run dev
```

### Windows App

```bash
cd windows-app
npm install
npm run electron:dev
```

### Android App

```bash
cd android-app
npm install
npx cap open android
```
