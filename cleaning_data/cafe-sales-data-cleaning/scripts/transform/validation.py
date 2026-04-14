import pandas as pd
import logging

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_dataframe(df):
  required_cols = [
    'transaction_date', 'item',
    'price_per_unit', 'quantity', 'total_spent'
  ]
  
  missing_cols = [col for col in required_cols if col not in df.columns]
  
  if missing_cols:
    raise ValueError(f"Missing columns: {missing_cols}")
  
  if df['price_per_unit'].lt(0).any():
    raise ValueError("Negative price_per_unit found")
  
  if df['quantity'].lt(0).any():
    raise ValueError("Negative quantity found")
  
  logging.info("DataFrame validation passed.")
  return df