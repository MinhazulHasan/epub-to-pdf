import os
from bs4 import BeautifulSoup
import json

def get_all_xml_folder_names(root_folder):
    folder_list = []
    for filename in os.listdir(root_folder):
        folder_list.append(filename)
    return folder_list

def parse_folder_to_json(folder_path, folder_name):
    # Iterate through files in the folder
    all_data = []
    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # Check if file is XHTML file and the file not equal toc.xhtml
        if filename.endswith('.xhtml') and filename != 'toc.xhtml':
            file_path = os.path.join(folder_path, filename)
            # Open and read XHTML file
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Parse HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Initialize dictionary to store data for this file
            data = {}

            # Get text from h1 tag as label
            h1_tag = soup.find('h1')
            if h1_tag:
                data['label'] = h1_tag.get_text()

            # Get text from all p tags as contentSource and make a string
            p_tags = soup.find_all('p')
            data['contentSource'] = ' '.join([p.get_text() for p in p_tags])

            # Add data for this file to the list
            all_data.append(data)

    output_dir = os.path.join('json-files', folder_name)
    os.makedirs(output_dir, exist_ok=True)
    # Write data for all files to JSON file
    with open(os.path.join(output_dir, 'output.json'), 'w', encoding="utf-8") as json_file:
        json.dump(all_data, json_file, indent=4)

# Usage
if __name__ == '__main__':
    folder_name = get_all_xml_folder_names('./xml-files')
    for folder in folder_name:
        parse_folder_to_json(f"./xml-files/{folder}/OEBPS/Text", folder)
