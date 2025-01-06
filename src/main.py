import os
import pandas as pd
from sentiment_analysis import SentimentAnalyzer
from image_processing import load_image, preprocess_image

def main(image_folder):
    analyzer = SentimentAnalyzer()
    results = []

    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(image_folder, image_file)
            image = load_image(file_path)
            processed_image = preprocess_image(image)
            emotions, highest_emotion = analyzer.analyze_sentiment(processed_image)
            if emotions:
                results.append({
                    'Image': image_file,
                    'Angry': emotions.get('angry', 0),
                    'Disgust': emotions.get('disgust', 0),
                    'Fear': emotions.get('fear', 0),
                    'Happy': emotions.get('happy', 0),
                    'Sad': emotions.get('sad', 0),
                    'Surprise': emotions.get('surprise', 0),
                    'Neutral': emotions.get('neutral', 0),
                    'Highest Emotion': highest_emotion
                })
                print(f"Image: {image_file}, Highest Emotion: {highest_emotion}")

    # Write results to an Excel file
    df = pd.DataFrame(results)
    df.to_excel('sentiment_analysis_results.xlsx', index=False)

if __name__ == "__main__":
    image_folder = r'C:/Users/leves/Downloads/faces for CV'  # Provide the path to your image folder
    main(image_folder)