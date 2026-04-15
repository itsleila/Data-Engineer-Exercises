import pandas as pd
import logging

def extract_data(file_path):
  try: 
    df = pd.read_csv(file_path)
    return df
  except Exception as e:
    logging.error(f"Error reading the file: {e}")
    raise