import pandas as pd
import logging

from transform.pipeline import transform
from load import load_data

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
  try:
    logging.info("Starting pipeline")

    df = load_data("data/raw/dirty_cafe_sales.csv")
    logging.info(f"Data loaded with {len(df)} rows")

    df_transformed = transform(df)
    logging.info("Data transformed successfully")

    df_transformed.to_csv("data/processed/cafe_sales.csv", index=False)
    logging.info("Data saved successfully")

  except Exception as e:
    logging.error(f"Pipeline failed: {e}")
    raise


if __name__ == "__main__":
  main()