
import base64
from PIL import Image
import io

def base64_to_image(base64_string, output_path):
    # Decode the base64 string
    image_data = base64.b64decode(base64_string)
    # Convert binary data to image
    image = Image.open(io.BytesIO(image_data))
    # Save image to a file or perform other operations
    image.save(output_path)
    return "Image successfully processed and saved."

def image_to_base64(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        # Read the file's content
        image_data = image_file.read()
    # Encode the binary data to base64
    base64_string = base64.b64encode(image_data).decode("utf-8")
    return base64_string
