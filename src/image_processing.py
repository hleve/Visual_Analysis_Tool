import os
import cv2

def load_images(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(directory, filename)
            image = cv2.imread(img_path)
            if image is not None:
                images.append((filename, image))
    return images

def load_image(file_path):
    image = cv2.imread(file_path)
    return image

def preprocess_image(image):
    # Resize and normalize the image as required by your model
    image = cv2.resize(image, (224, 224))  # Example size, adjust as needed
    image = image / 255.0  # Normalize to [0, 1]
    return image