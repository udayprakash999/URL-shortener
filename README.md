# URL Shortener

This is a simple Python-based GUI application for shortening URLs. It provides an intuitive interface to shorten long URLs using services like TinyURL and Is.gd. The application also includes additional features such as copying the shortened URL to the clipboard, clearing fields, and saving the shortened URLs to a file.

## Features

1. **URL Shortening**: Shorten long URLs using TinyURL or Is.gd services.
2. **Copy to Clipboard**: Copy the shortened URL to the clipboard with a single click.
3. **Clear Fields**: Clear all input and output fields to reset the form.
4. **Save URL**: Save the long URL and its shortened version to a text file (`shortened_urls.txt`).
5. **Error Handling**: Displays an error message if an invalid URL or service is selected.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `pyshorteners` library

## Usage

1. Launch the application by running the script.
2. Enter the long URL in the "Enter Long URL" field.
3. Select a shortening service (TinyURL or Is.gd) from the dropdown menu.
4. Click on the "Shorten URL" button to generate the shortened URL.
5. Use the "Copy to Clipboard" button to copy the shortened URL to your clipboard.
6. Use the "Clear" button to reset the form.
7. Use the "Save URL" button to save the long and shortened URLs to a file named `shortened_urls.txt`.

## File Details

- **shortened_urls.txt**: This file stores the long and shortened URLs in the format:
  ```
  <long_url> -> <shortened_url>
  ```

## Example

### Input
- Long URL: `https://example.com/some/long/path`
- Selected Service: `TinyURL`

### Output
- Shortened URL: `https://tinyurl.com/abcd1234`

## Error Handling

- If an invalid URL is entered, the application will display an error message: `Invalid URL or Service. Please try again.`
- Ensure that you select a valid service from the dropdown.

Happy URL shortening! 🎉
