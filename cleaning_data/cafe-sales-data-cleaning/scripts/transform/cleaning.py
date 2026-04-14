import pandas as pd
import logging

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def normalize_column_names(df):
  try:
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    logging.info("Column names normalized successfully.")
    return df
  except Exception as e:
    logging.error(f"Error normalizing column names: {e}")
    raise

def convert_columns(df, datetime_cols=None, numeric_cols=None, int_cols=None):
  try:
    df = df.copy()
    
    if datetime_cols:
      for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    if numeric_cols:
      for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    if int_cols:
      for col in int_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')

    logging.info("Columns converted successfully.")
    return df
  
  except Exception as e:
    logging.error(f"Error converting columns: {e}")
    raise


def replace_values(df, replace_dict):
  try:
    df = df.copy()
    for col, mapping in replace_dict.items():
      df[col] = df[col].replace(mapping)

    logging.info("Values replaced successfully.")
    return df
  except Exception as e:
    logging.error(f"Error replacing values: {e}")
    raise

def map_item_and_price(df, fill_dict):
  try:
    df = df.copy()
    for col, value in fill_dict.items():
      df[col] = df[col].fillna(value)
    logging.info("Missing values filled successfully.")
    return df
  except Exception as e:
    logging.error(f"Error filling missing values: {e}")
    raise


def fill_missing_with_unknown(df, cols):
  try:
    df = df.copy()
    for col in cols:
      df[col] = df[col].fillna('Unknown')
    logging.info("Missing values filled with 'Unknown' successfully.")
    return df
  except Exception as e:
    logging.error(f"Error filling missing values with 'Unknown': {e}")
    raise


def drop_nulls(df, subset=None):
  try:
    df = df.copy()
    df = df.dropna(subset=subset)
    logging.info(f"Null values dropped successfully for subset: {subset}")
    return df
  except Exception as e:
    logging.error(f"Error dropping null values: {e}")
    raise