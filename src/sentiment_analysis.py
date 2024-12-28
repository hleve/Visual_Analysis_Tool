import numpy as np
import tensorflow as tf
import cv2

class SentimentAnalyzer:
    def __init__(self):
        # Load your pre-trained model here
        self.model = tf.keras.models.load_model('path/to/your/model')

    def analyze_sentiment(self, image):
        # Predict sentiment score using the model
        prediction = self.model.predict(np.expand_dims(image, axis=0))
        sentiment_score = np.argmax(prediction) + 1  # Assuming the model outputs scores from 0 to 4
        sentiment_label = self.get_sentiment_label(sentiment_score)
        return sentiment_score, sentiment_label

    def get_sentiment_label(self, score):
        labels = {1: 'Very Negative', 2: 'Negative', 3: 'Neutral', 4: 'Positive', 5: 'Very Positive'}
        return labels.get(score, 'Unknown')

def load_image(file_path):
    image = cv2.imread(file_path)
    return image

def preprocess_image(image):
    # Resize and normalize the image as required by your model
    image = cv2.resize(image, (224, 224))  # Example size, adjust as needed
    image = image / 255.0  # Normalize to [0, 1]
    return image