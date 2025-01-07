# Sentiment Analysis on Images

This project performs sentiment analysis on a sequence of images using computer vision techniques. Each image is assigned a sentiment score in the form of a percentage across categories of Angry, Disgust, Fear, Happy, Sad, Surprise, and Neutral using the fer library from Justin Shenk https://github.com/JustinShenk/fer
The code generates an Excel file with the image name, the percentages for each emotion, and the dominant emotion.

## Project Structure

```
sentiment-analysis-project
├── main.py                # Entry point of the application
├── requirements.txt       # Project dependencies
├── .gitignore             # Files and directories to ignore in Git
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hleve/Visual_Analysis_Tool
   cd sentiment-analysis-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   On Windows:
   ```
   venv\Scripts\activate
   ```

   On macOS and Linux:
   ```
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```


## Usage

1. Place your images in a designated directory.
2. Update the image directory path in `main.py`.
3. Run the application:
   ```
   python main.py
   ```

## Output

The application will generate an Excel file containing the image names and their corresponding sentiment scores.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
