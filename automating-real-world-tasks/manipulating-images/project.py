"""
Use the Python Imaging Library to do the following to a batch of images:
Open an image
Rotate an image
Resize an image
Save an image in a specific format in a separate directory 
"""

from pathlib import Path
from PIL import Image

# Define the directory path
folder_path = Path("./images")
updated_folder_path = Path("/opt/icons")

#Create directory if it does not exist
updated_folder_path.mkdir(parents=True, exist_ok=True)

# Define acceptable image extensions
image_extensions = {".tiff"}

# Loop through all files in the directory
for counter, file_path in enumerate(folder_path.iterdir(), start=1):
    # if file_path.suffix.lower() in image_extensions:
        print(f"Processing: {file_path.name}")
        
        # Open the image
        with Image.open(file_path) as img:
            # Perform your image operations here
            # Rotate the image by 90 degrees
            rotated_img = img.rotate(90)
            # resize to 128x128
            resized_img = rotated_img.resize((128, 128))

            #Change LA mode to RGB mode to save in jpg format
            resized_img = resized_img.convert("RGB")
            # Create a different name for each image
            output_file = updated_folder_path / f"image{counter}.jpg"

            #Save image in a specific format (jpg) in directory /opt/icons/
            resized_img.save(output_file, "JPEG")