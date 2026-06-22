# MathBeast - Windows App

This is the Windows desktop version of the MathBeast, written in Python using Flet.

## How to get .exe output

To build the Windows executable, you need to have Python and the Flet CLI installed.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build EXE:**
   Run the following command from the root directory, pointing to the `app/` folder:
   ```bash
   flet build windows app/
   ```

The resulting `.exe` file and its dependencies will be generated in the `build/windows` directory.

## Development

To run the app in development mode:
```bash
flet run app/main.py
```
