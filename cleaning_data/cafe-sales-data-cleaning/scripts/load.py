import sqlite3
import pandas as pd
import logging

def load_data_to_csv(df,file_path):
  try:
    df.to_csv(file_path, index=False)
    logging.info(f"Data saved to {file_path} successfully")
  except Exception as e:
    logging.error(f"Failed to save data to CSV: {e}")
    raise


def connect_to_sqlite(db_path):
  try:
    conn = sqlite3.connect(db_path)
    logging.info(f"Connected to SQLite database at {db_path}")
    return conn
  except Exception as e:
    logging.error(f"Failed to connect to SQLite database: {e}")
    raise


def load_data_to_sqlite(df, db_path, table_name):
  try:
    conn = connect_to_sqlite(db_path)
    logging.info(f"Loading data into SQLite database at {db_path}, table: {table_name}")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    logging.info("Data loaded into SQLite successfully")
  except Exception as e:
    logging.error(f"Failed to load data into SQLite: {e}")
    raise
  finally:
    conn.close()