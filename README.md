# Favicon Generator

Generates a favicon.ico containing a single letter with customizable colors.

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/)  
  Install with:
  ```bash
  pip install Pillow
  ```

## Font Dependency

This script attempts to use `arial.ttf`.  
- On Windows, Arial is usually pre-installed.  
- On Linux, install it via:
  ```bash
  sudo apt update
  sudo apt install ttf-mscorefonts-installer
  ```  
If not found, the script falls back to a default font and issues a warning.

## Usage

Run the script with three required parameters and an optional fourth:

```bash
python gen.py <letter> <background_color> <foreground_color> [output_filename]
```

- **letter**: Single character to display.  
- **background_color**: Accepts standard color names, hex codes (e.g., `"#FFFFFF"`), or RGB tuples.  
- **foreground_color**: Color for the letter, in any accepted format.  
- **output_filename**: Output ICO file name (default is `favicon.ico`).

### Example

```bash
python gen.py A "#FFFFFF" "#000000" myfavicon.ico
```

This generates a 64×64 favicon with a white background, a black letter "A", and saves it as `myfavicon.ico`.

## Script Details

- **Image size**: 64×64 pixels  
- **Font size**: 48  
- **Text centering**: The letter is centered horizontally and adjusted vertically by 8 pixels.  
- **Fallback**: If `arial.ttf` is unavailable, a default font is used.

## Note

The current argument parsing expects exactly 4 arguments (script name plus three or four parameters). Adjust the code if you need different behavior for optional arguments.
