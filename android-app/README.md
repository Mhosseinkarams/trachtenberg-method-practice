# Fast Math Trainer - Android App

This is the Android version of the Fast Math Trainer, written in Python using Flet.

## How to get .apk output

To build the Android APK, you need to have Python and the Flet CLI installed.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build APK:**
   Run the following command from the root directory, pointing to the `app/` folder:
   ```bash
   flet build apk app/
   ```

The resulting `.apk` file will be generated in the `build/apk` directory.

## Development

To run the app in development mode:
```bash
flet run app/main.py
```
