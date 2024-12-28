# FILE: /sentiment-analysis-project/sentiment-analysis-project/src/utils/__init__.py
def write_to_excel(data, file_name):
    import pandas as pd

    df = pd.DataFrame(data, columns=['Image Name', 'Sentiment Score'])
    df.to_excel(file_name, index=False)