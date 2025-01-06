import cv2
from fer import FER
import tensorflow as tf

# Suppress TensorFlow warnings
tf.get_logger().setLevel('ERROR')

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the FER detector
        self.detector = FER()

    def analyze_sentiment(self, image):
        # Detect emotions in the image
        result = self.detector.detect_emotions(image)
        if result:
            emotions = result[0]['emotions']
            highest_emotion = max(emotions, key=emotions.get)
            return emotions, highest_emotion
        else:
            return None, 'Unknown'