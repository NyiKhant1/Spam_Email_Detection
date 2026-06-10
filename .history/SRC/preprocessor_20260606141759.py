import re

def convert_to_clean_text(df, columns):
    for column in columns:
        df[column] = (
            df[column]
            .fillna('')
            .astype(str)
            .str.lower()
            # .str.replace(r'[^\w\s]', '', regex=True)
            .str.strip()
        )
    return df