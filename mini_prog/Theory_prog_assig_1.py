# Mini Programming Assignment 1
# CS 3378
# Juan Banda 10/14/24

import re
import os

def extract_details(html_content, output_file):
    # Regular expressions tailored to specific HTML class structures
    name_pattern = re.compile(r'<div class="name">\s*(.*?)\s*</div>', re.IGNORECASE)
    title_department_pattern = re.compile(r'<div class="first-appointment">\s*(.*?)\s*&mdash;\s*(.*?)\s*</div>', re.IGNORECASE)
    office_pattern = re.compile(r'<div class="office">\s*(.*?)\s*</div>', re.IGNORECASE)
    phone_pattern = re.compile(r"phone:\s*\(?(\d{3})\)?[-.\s]*(\d{3})[-.\s]*(\d{4})", re.IGNORECASE)
    email_pattern = re.compile(r'href="mailto:(.*?)"', re.IGNORECASE)

    # Extract each detail
    name = name_pattern.search(html_content)
    title_department = title_department_pattern.search(html_content)
    office = office_pattern.search(html_content)
    phone = phone_pattern.search(html_content)
    email = email_pattern.search(html_content)

    # Extract title and department separately if found
    title = title_department.group(1) if title_department else "Not Found"
    department = title_department.group(2) if title_department else "Not Found"
    
    # Format the phone number if found
    formatted_phone = f"({phone.group(1)}) {phone.group(2)}-{phone.group(3)}" if phone else "Not Found"

    # Write the extracted details to the output file
    output_file.write("Name: " + (name.group(1) if name else "Not Found") + "\n")
    output_file.write("Title: " + title + "\n")
    output_file.write("Department: " + department + "\n")
    output_file.write("Office: " + (office.group(1) if office else "Not Found") + "\n")
    output_file.write("Phone: " + formatted_phone + "\n")
    output_file.write("Email: " + (email.group(1) if email else "Not Found") + "\n")
    output_file.write("-" * 40 + "\n")  # Separator for better readability

# Get the current directory where the script is located
directory_path = os.getcwd()

# Open the output text file in write mode
with open('extracted_details.txt', 'w', encoding='utf-8') as output_file:
    # Loop through each HTML file in the current directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.html'):  # Only process HTML files
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    html_content = file.read()
                    output_file.write(f"Processing {filename}...\n")  # Indicate which file is being processed
                    extract_details(html_content, output_file)
            except Exception as e:
                output_file.write(f"Error reading {filename}: {e}\n")
