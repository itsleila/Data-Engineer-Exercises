import pandas as pd
import logging

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)


def fill_unknown_items_by_price(df, price_map):
  try:
    df = df.copy()
    
    for price, label in price_map.items():
      mask = df['item'].isna() & (df['price_per_unit'] == price)
      df.loc[mask, 'item'] = label
    
    logging.info("Filled unknown items based on price successfully.")
    return df
  except Exception as e:
    logging.error(f"Error filling unknown items by price: {e}")
    raise


def handle_quantity_and_total_spent(df):
  try:
    df = df.copy()
    
    df['quantity'] = df['quantity'].apply(
      lambda x: x if pd.isna(x) else round(x)
    )

    mask_total = df['total_spent'].isna() & df['quantity'].notna()
    df.loc[mask_total, 'total_spent'] = (
      df.loc[mask_total, 'price_per_unit'] * df.loc[mask_total, 'quantity']
    )
    
    mask_quantity = df['quantity'].isna() & df['total_spent'].notna()
    df.loc[mask_quantity, 'quantity'] = (
      df.loc[mask_quantity, 'total_spent'] / df.loc[mask_quantity, 'price_per_unit']
    )
    
    logging.info("Handled quantity and total spent successfully.")
    return df
  except Exception as e:
    logging.error(f"Error handling quantity and total spent: {e}")
    raise