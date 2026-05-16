# Fast Math Trainer - Multi-Platform

A comprehensive mental math training application supporting Trachtenberg and Vedic methods.

## Project Structure

- `web-app/`: The core web application built with React and Vite.
- `windows-app/`: Windows desktop application using Electron.
- `android-app/`: Android mobile application using Capacitor.
- `windows-app-cpp/`: CLI-based C++ implementation for Windows.

## Binary Artifacts

- **Windows EXE**: `windows-app-cpp/FastMathTrainer.exe`
- **Android APK**: `android-app/android/app/build/outputs/apk/debug/app-debug.apk`

## Features

- **Trachtenberg System**: Multiplication by 11, 12, 5, and Rapid Addition.
- **Vedic Mathematics**: Squaring (ending in 5, general method), Square Root (perfect squares), and Complementary Addition.
- **Multi-platform support**: Native-like experience on Web, Desktop (Electron & C++), and Mobile (Android).

## Getting Started

### Web App
```bash
cd web-app
npm install
npm run dev
```

### Windows C++ App
Build with MinGW:
```bash
cd windows-app-cpp
make
```

### Android App
Build APK:
```bash
cd android-app
npm install
npm run build
npx cap sync
cd android && ./gradlew assembleDebug
```
