
```markdown
# persian_pdf_converter

A Python package for converting PDF files to Word documents and modifying URLs. This package utilizes Tesseract OCR for text recognition in PDF files.

## Features

- Convert PDF files to Word documents with text recognition
- Modify URLs based on directory paths

## Requirements

- Python 3.6 or higher
- Tesseract OCR installed and configured

## Installation

To install the package, use pip:

```bash
pip install persian-pdf-converter
```

### Install Tesseract

For the `pdf_to_word` function to work correctly, you need to have Tesseract OCR installed. You can download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract). After installation, make sure Tesseract's binary path is added to your system's PATH.

For Windows:
```bash
setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"
```

For Unix-based systems (Linux, macOS):
```bash
export PATH=$PATH:/usr/local/bin
```

## Usage

Here is an example of how to use the functions provided by this package:

```python
from persian_pdf_converter.pdf_converter import pdf_to_word

# Path to your PDF file and output directory
pdf_path = 'path/to/example.pdf'
output_dir = 'path/to/output/dir'

# Convert PDF to Word
output_file = pdf_to_word(pdf_path, output_dir, lang="fas+eng", dpi=300)
print(f"Converted file saved as: {output_file}")
```

### pdf_to_word Function

This function converts a PDF file to a Word document with text recognition.

#### Parameters:

- `pdf_path` (str): Path to the PDF file.
- `output_dir` (str): Directory where the output Word file will be saved.
- `lang` (str): Languages to be used by Tesseract for text recognition (default is `"fas+eng"`).
- Additional keyword arguments for `convert_from_path`.

#### Returns:

- `str`: Name of the output Word file.



## Development

To contribute to this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mahdiramezanii/persian_pdf_converter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd persian_pdf_converter
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Make your changes and run tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact me at [your-email@example.com](mailto:your-email@example.com).
