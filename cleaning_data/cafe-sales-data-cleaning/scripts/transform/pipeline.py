from .validation import validate_dataframe
from .cleaning import normalize_column_names, convert_columns,fill_missing_with_unknown, replace_values, map_item_and_price, drop_nulls
from .business_rules import fill_unknown_items_by_price, handle_quantity_and_total_spent
import logging



replacements = {
  'item': {'UNKNOWN': None, 'ERROR': None},
  'payment_method': {'UNKNOWN': None, 'ERROR': None},
  'location': {'UNKNOWN': None, 'ERROR': None},
}

replacements_item_and_price = {
 'item': {
  'Cookie': 1.0,
  'Tea': 1.5,
  'Coffee': 2.0,
  'Salad': 5.0,
  'Juice': 3.0,
  'Cake': 3.0,
  'Smoothie': 4.0,
  'Sandwich': 4.0
},
'price_per_unit': {
  1.0: 'Cookie',
  1.5: 'Tea',
  2.0: 'Coffee',
  5.0: 'Salad'

}
}

price_map = {
  3.0: 'Unknown_3.0',
  4.0: 'Unknown_4.0'
}


def transform(df):
  logging.info("Starting data transformation.")
  df = normalize_column_names(df)
  
  df = validate_dataframe(df)
  
  df = convert_columns(
    df,
    numeric_cols=['price_per_unit', 'total_spent'],
    int_cols=['quantity'],
    datetime_cols=['transaction_date']
  )
  
  df = replace_values(df, replacements)
  
  df = fill_missing_with_unknown(df, ['payment_method', 'location', 'item'])
  
  df = map_item_and_price(df, replacements_item_and_price)
  
  df = fill_unknown_items_by_price(df, price_map)
  
  df = handle_quantity_and_total_spent(df)
  
  df = drop_nulls(
    df,
    subset=['transaction_date', 'item', 'price_per_unit', 'quantity', 'total_spent']
  )
  logging.info("Data transformation completed successfully.")
  return df