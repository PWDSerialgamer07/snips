import base64
import json
import os

# Load your .excalidraw file
with open("export.excalidraw", "r") as file:
    data = json.load(file)

# Create a folder to save the images if it doesn't exist
os.makedirs("output", exist_ok=True)

# Loop through the files in the 'files' object
for file_id, file_data in data.get("files", {}).items():
    if 'dataURL' in file_data:
        # Extract the base64 string (remove the 'data:image/jpeg;base64,' part)
        base64_data = file_data['dataURL'].split(',')[1]

        # Decode the base64 string into binary data
        img_data = base64.b64decode(base64_data)

        # Get the MIME type (e.g., image/jpeg) and determine the file extension
        mime_type = file_data['mimeType']
        if mime_type == "image/jpeg":
            file_extension = "jpg"
        elif mime_type == "image/png":
            file_extension = "png"
        else:
            file_extension = "img"  # Fallback for unknown types

        # Save the image to the extracted_images folder
        with open(f"output/{file_id}.{file_extension}", "wb") as img_file:
            img_file.write(img_data)

print("Images extracted successfully.")
