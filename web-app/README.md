# MathBeast - Web App

This is the web version of the MathBeast, written in Python using Flet.

## How to get web output

To build the web application, you need to have Python and the Flet CLI installed.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build Web:**
   Run the following command from the root directory, pointing to the `app/` folder:
   ```bash
   flet build web app/
   ```

The resulting web static files will be generated in the `build/web` directory.

## Development

To run the app as a web app in development mode:
```bash
flet run app/main.py --web
```
