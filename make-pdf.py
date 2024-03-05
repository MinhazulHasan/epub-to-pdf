import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def get_all_json_folder_names(root_folder):
    folder_list = []
    for filename in os.listdir(root_folder):
        folder_list.append(filename)
    return folder_list


def generate_pdf_from_json(folder):
    # Initialize list to store content
    content = []

    # Open and load JSON file
    with open(os.path.join('./json-files', folder, 'output.json'), 'r', encoding="utf8") as f:
        data = json.load(f)

    styles = getSampleStyleSheet()
    # Iterate through each object in JSON data
    for obj in data:
        # Extract label and content source
        label = obj.get('label', '')
        content_source = obj.get('contentSource', '')
        
        # Add label as heading and content source as description
        # remove all special character and brackets from label and content source 
        label = label.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("<", "").replace(">", "").replace("*", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace("-", "").replace("_", "").replace("=", "").replace("+", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")

        content_source = content_source.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("<", "").replace(">", "").replace("*", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace("-", "").replace("_", "").replace("=", "").replace("+", "").replace("&", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")

        content.append(Paragraph(f"TITLE: <b>{label}</b>", styles['Heading3']))
        content.append(Paragraph(content_source, styles['Normal']))
        content.append(Paragraph("<br/><br/>", styles['Normal']))

    return content


if __name__ == "__main__":
    folder_name = get_all_json_folder_names('./json-files')
    doc = SimpleDocTemplate('output.pdf', pagesize=letter)
    content = []

    for folder in folder_name:
        json_content = generate_pdf_from_json(folder)
        content.extend(json_content)

    doc.build(content)
