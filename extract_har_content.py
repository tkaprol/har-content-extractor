import json
import base64
from pathlib import Path

def extract_content(har_path, output_folder):
    # Load HAR file
    with open(har_path, 'r') as file:
        har_data = json.load(file)

    # Ensure output directory exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through the entries
    for entry in har_data['log']['entries']:
        # Check if the response has content
        content = entry['response'].get('content', {})
        if 'text' in content and 'encoding' in content and content['encoding'] == 'base64':
            # Decode the base64 content
            file_content = base64.b64decode(content['text'])
            # Generate a filename (you might want to customize this part)
            file_name = f"{entry['startedDateTime'].replace(':', '-').replace('T', '_').split('.')[0]}_{content['size']}.{content['mimeType'].split('/')[-1]}"
            file_path = Path(output_folder) / file_name

            # Save the content to a file
            with open(file_path, 'wb') as file:
                file.write(file_content)
            print(f"Saved {file_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python extract_har_content.py [HAR file path] [Output folder]")
    else:
        har_path = sys.argv[1]
        output_folder = sys.argv[2]
        extract_content(har_path, output_folder)
