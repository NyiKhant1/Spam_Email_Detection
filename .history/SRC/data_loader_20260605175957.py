import os 

def load_data (path):
    if not os.path.exists(path):
        raise FileNotFoundError