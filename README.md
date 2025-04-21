# Sentiment Analysis for Images

This project performs sentiment analysis on a sequence of images using computer vision techniques. Each image is assigned a sentiment score in the form of a percentage across categories of Angry, Disgust, Fear, Happy, Sad, Surprise, and Neutral, the universal basic emotions defined by Psychologist Paul Ekman, using the fer library from Justin Shenk https://github.com/JustinShenk/fer
The code generates an Excel file with the image name, the percentages for each emotion, and the dominant emotion.

## Project Structure

```
sentiment-analysis
├── main.py                # Entry point of the application
├── requirements.txt       # Project dependencies
├── .gitignore             # Files and directories to ignore in Git
├── example_images         # folder with example images
├── example_results.xlsx   # example results from running the example images
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hleve/Visual_Analysis_Tool
    ```

2. Navigate to the cloned directory:
   ```
   cd sentiment-analysis
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:
   ```
   venv\Scripts\activate
   ```

   On macOS and Linux:
   ```
   source venv/bin/activate
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Run the python file:
   ```
   python3 main.py
   ```


## Usage

1. Place your images in a designated directory.
2. Navigate to the designated directory
3. Update the image directory path in `main.py`.
4. Update the output directory path in `main.py`.
5. Run the application:

   ```
   python main.py
   ```

## Output

The application will generate an Excel file containing the image names and their corresponding sentiment scores.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
