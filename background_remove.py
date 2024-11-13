from rembg import remove
from PIL import Image
import io


def remove_background(input_path, output_path):
    # Open the image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    # Remove the background
    output_data = remove(input_data)

    # Save the result
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

    print(f"Background removed image saved at: {output_path}")


# Usage example
input_image = 'girl.png'  # Replace with your image file
output_image = 'output_image3.png'  # Output with transparent background
remove_background(input_image, output_image)
