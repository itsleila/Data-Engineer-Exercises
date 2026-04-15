import pandas as pd
import logging
from extract import extract_data
from transform.pipeline import transform
from load import load_data_to_csv, load_data_to_sqlite

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

PATH_RAW_DATA = "data/raw/dirty_cafe_sales.csv"
PATH_PROCESSED_DATA = "data/processed/cafe_sales.csv"
PATH_SQLITE_DB = "db/cafe_sales.db"
TABLE_NAME = "sales"

def main():
  try:
    logging.info("Starting pipeline")

    df = extract_data(PATH_RAW_DATA)
    logging.info(f"Data loaded with {len(df)} rows")

    df_transformed = transform(df)
    logging.info("Data transformed successfully")

    load_data_to_csv(df_transformed, PATH_PROCESSED_DATA)
    logging.info("Data saved successfully")

    load_data_to_sqlite(df_transformed, PATH_SQLITE_DB, TABLE_NAME)
    logging.info("Data loaded into SQLite successfully")
  except Exception as e:
    logging.error(f"Pipeline failed: {e}")
    raise


if __name__ == "__main__":
  main()