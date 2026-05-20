# MathBeast - Unified Python Platform

A comprehensive mental math training application supporting Trachtenberg and Vedic methods. This repository has been unified to use Python for all platforms.

## Project Structure

- `app/`: **Core source code** (Flet-based UI and Math Logic).
- `web-app/`: Build instructions for the Web platform.
- `windows-app/`: Build instructions for the Windows desktop platform.
- `android-app/`: Build instructions for the Android mobile platform.
- `windows-cli-app/`: Command-line interface version of the trainer.

## Features

- **Trachtenberg System**: Multiplication by 11, 12, 5, and Rapid Addition.
- **Vedic Mathematics**: Squaring (ending in 5, general method), Square Root (perfect squares), and Complementary Addition.
- **Multi-platform support**: Unified codebase for Web, Desktop, and Mobile using Flet.

## Getting Started

To run the application locally on any platform, ensure you have Python and Flet installed:

```bash
pip install -r requirements.txt
```

Then, run the main app:
```bash
flet run app/main.py
```

Or run the CLI version:
```bash
python windows-cli-app/main.py
```

## Building for Specific Platforms

For detailed instructions on how to generate `.exe`, `.apk`, or web output, please refer to the `README.md` file within each respective directory:

- **Android APK**: See [android-app/README.md](android-app/README.md)
- **Windows EXE**: See [windows-app/README.md](windows-app/README.md)
- **Web App**: See [web-app/README.md](web-app/README.md)
