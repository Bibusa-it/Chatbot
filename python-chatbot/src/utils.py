def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def preprocess(text):
    import re
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text.strip()