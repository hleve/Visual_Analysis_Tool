import os
import pandas as pd
from sentiment_analysis import SentimentAnalyzer
from utils.image_processing import load_image, preprocess_image

def main(image_folder):
    analyzer = SentimentAnalyzer()
    results = []

    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(image_folder, image_file)
            image = load_image(file_path)
            processed_image = preprocess_image(image)
            sentiment_score, sentiment_label = analyzer.analyze_sentiment(processed_image)
            results.append({'Image': image_file, 'Sentiment Score': sentiment_score, 'Sentiment Label': sentiment_label})
            print(f"Image: {image_file}, Sentiment Score: {sentiment_score}, Sentiment Label: {sentiment_label}")

    # Write results to an Excel file
    df = pd.DataFrame(results)
    df.to_excel('sentiment_analysis_results.xlsx', index=False)

if __name__ == "__main__":
    image_folder = 'path/to/your/image/folder'  # Update this path
    main(image_folder)