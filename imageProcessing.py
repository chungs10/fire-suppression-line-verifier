import numpy as np
import cv2
import os
import base64
from PIL import Image
from io import BytesIO
from keras.models import load_model
model = load_model('united_model_v1.h5')

def image_to_array(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if image reading was successful
    if image is None:
        raise ValueError(f"Error reading image from path: {image_path}")

    # Convert the image to a NumPy array
    image_array = np.asarray(image)

    return image_array

def preprocess_image(image_arr, image_size):
    img = image_arr
    img = cv2.resize(img, image_size)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0  # Normalize pixel values to [0, 1]
    img = np.transpose(img, (1, 0, 2))  # Transpose the image to match the expected input shape
    return np.expand_dims(img, axis=0)  # Add batch dimension

def process_and_save_image(image_path, state):
    # Read the image
    image = cv2.imread(image_path)
    # Extract the directory path and file name without extension
    directory_path, file_name = os.path.split(image_path)
    file_name_without_extension, extension = os.path.splitext(file_name)

    # Check if image reading was successful
    if image is None:
        raise ValueError(f"Error reading image: {image_path}")

    if state == 0:
        # Write "Pass" on the image in green
        text_color = (0, 255, 0)  # Green color
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 5
        thickness = 20
        text = "Pass"
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int((image.shape[1] - text_size[0]) / 2)  # Centered horizontally
        text_y = int((image.shape[0] + text_size[1]) / 2)  # Centered vertically
        cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, thickness)

        # Draw a green box around the border of the image
        box_color = (0, 255, 0)  # Green color
        thickness = 20
        cv2.rectangle(image, (0, 0), (image.shape[1] - 1, image.shape[0] - 1), box_color, thickness)

        # Save the processed image
        new_file_name = f"{file_name_without_extension}__pass{extension}"
        new_file_path = os.path.join(directory_path.replace("unprocessed", "processed"), new_file_name)
        cv2.imwrite(new_file_path, image)
        return new_file_path
        
    else:
        text_color = (0, 0, 255)  # Red color
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 10
        thickness = 20
        text = "Fail"
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = int((image.shape[1] - text_size[0]) / 2)  # Centered horizontally
        text_y = int((image.shape[0] + text_size[1]) / 2)  # Centered vertically
        cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, thickness)

        # Draw a green box around the border of the image
        box_color = (0, 0, 255)
        thickness = 20
        cv2.rectangle(image, (0, 0), (image.shape[1] - 1, image.shape[0] - 1), box_color, thickness)

        # Save the processed image
        new_file_name = f"{file_name_without_extension}__fail{extension}"
        new_file_path = os.path.join(directory_path.replace("unprocessed", "processed"), new_file_name)
        cv2.imwrite(new_file_path, image)
        return new_file_path

def base64_to_image(base64_string, output_path):
    base64_string = base64_string.split(',')[1]
    # Decode the base64 string to bytes
    image_bytes = base64.b64decode(base64_string)

    # Open the image using PIL
    image = Image.open(BytesIO(image_bytes))

    # Save the image to the specified output path
    image.save(output_path)

def main(image_path):
    # Preprocess the image
    img_arr = image_to_array(image_path)
    preprocessed_image = preprocess_image(img_arr, image_size=(369, 573))

    # Make predictions using the trained model
    predictions = model.predict(preprocessed_image)[0][0]
    result = process_and_save_image(image_path, predictions)
    return result
    
if __name__ == '__main__':
    pass