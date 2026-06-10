import os 
import pandas as pd

def load_data (path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found")

    df = pd.read_csv(path)