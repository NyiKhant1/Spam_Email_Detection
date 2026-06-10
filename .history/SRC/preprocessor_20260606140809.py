import re 

def convert_to_clean_text(df, columns):
    for column in columns:
        df[column] = df[column].str.lower()
        df[co]
