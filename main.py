import cv2
from fer import FER
import os
import pandas as pd

# Folder containing the images - Update this to the folder containing your images
image_folder = "C:/Users/..."

# Initialize the emotion detector with MTCNN
emotion_detector = FER(mtcnn=True)

# List to store the results
results = []

# Loop through all files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Read the input image
        input_image = cv2.imread(os.path.join(image_folder, filename))
        
        # Detect emotions and store the result
        result = emotion_detector.detect_emotions(input_image)
        if result:
            emotions = result[0]['emotions']
            highest_emotion = max(emotions, key=emotions.get)
            results.append({
                'Image': filename,
                'Angry': emotions.get('angry', 0),
                'Disgust': emotions.get('disgust', 0),
                'Fear': emotions.get('fear', 0),
                'Happy': emotions.get('happy', 0),
                'Sad': emotions.get('sad', 0),
                'Surprise': emotions.get('surprise', 0),
                'Neutral': emotions.get('neutral', 0),
                'Highest Emotion': highest_emotion
            })
            print(f"Image: {filename}, Highest Emotion: {highest_emotion}")

# Create a DataFrame from the results
df = pd.DataFrame(results)

# Save the DataFrame to an Excel file - Update this line with where your file will be output.
output_file = "C:/Users/emotion_analysis_results.xlsx"
df.to_excel(output_file, index=False)

print(f"Results saved to {output_file}")
