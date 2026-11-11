# NoixyDev Official Website

A small multilingual portfolio website built with Python and Flask.

## Languages
- Turkish (`/?lang=tr`)
- English (`/?lang=en`)
- Russian (`/?lang=ru`)

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the website:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

The site starts in Turkish. Use the TR / EN / RU buttons to change language.

## Notes
- This is a starter project for local development.
- Before publishing, review every biography detail and remove any personal information you do not want public.
- For public hosting, turn off Flask debug mode and use a production WSGI server.
