# HAR Content Extractor

This Python script is designed to extract binary content (such as images, audio, and videos) encoded in base64 from HTTP Archive (HAR) files and save them as separate files. It's particularly useful for developers and analysts working with web applications, allowing them to easily extract downloaded resources from web traffic for further analysis or debugging.

## Features

- Extracts binary files encoded in base64 from HAR files.
- Supports various binary content types (images, audio, etc.).
- Automatically generates filenames based on the content's MIME type and the timestamp.

## Prerequisites

Before you run this script, ensure you have Python 3.x installed on your system. You can verify the installation by running `python3 --version` in your terminal.

## Usage

To use the HAR Content Extractor, follow these steps:

1. Clone or download this repository to your local machine.
2. Open your terminal and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python3 extract_har_content.py path/to/your/har_file.har path/to/output/directory
