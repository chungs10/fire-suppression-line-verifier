# load json and create model
import numpy as np
import cv2
from tensorflow.keras.models import Sequential, model_from_json

json_file = open('united_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("united_model.weights.h5")
print("Loaded model from disk")

loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

def image_to_array(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if image reading was successful
    if image is None:
        raise ValueError(f"Error reading image from path: {image_path}")

    # Convert the image to a NumPy array
    image_array = np.asarray(image)

    return image_array

path = 'static/database/template/luaggage_image0_class0.jpg'
img = image_to_array(path)
im = img.reshape(1,369, 573, 3)
im = im/255.0

prediction = loaded_model.predict(im)
prediction = (prediction > 0.5).astype(int)[0][0] ## return image as integer
print(prediction)



# predictions_loaded = []
# for im in X_test_normalized:
#     im = im.reshape(1,369, 573, 3)
#     pred = loaded_model.predict(im)

#     pred = (pred > 0.5).astype(int)
#     print(pred[0][0])

#     predictions_loaded.append(pred[0][0])