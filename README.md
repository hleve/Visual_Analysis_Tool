# Sentiment Analysis on Images

This project performs sentiment analysis on a sequence of images using computer vision techniques. Each image is assigned a sentiment score ranging from 1 to 5, and the results are saved in an Excel file.

## Project Structure

```
sentiment-analysis-project
├── src
│   ├── main.py                # Entry point of the application
│   ├── sentiment_analysis.py   # Contains the SentimentAnalyzer class
│   ├── image_processing.py     # Functions for loading and preprocessing images
│   └── utils
│       └── __init__.py        # Utility functions for the project
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files and directories to ignore in Git
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sentiment-analysis-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your images in a designated directory.
2. Update the image directory path in `src/main.py`.
3. Run the application:
   ```
   python src/main.py
   ```

## Output

The application will generate an Excel file containing the image names and their corresponding sentiment scores.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.