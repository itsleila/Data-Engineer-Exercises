#%%
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

#%%

def get_connection():
  try:
    return psycopg2.connect(
      database="ecommerce",
      user=os.getenv("DATABASE_USER"),
      password=os.getenv("DATABASE_PASSWORD"),
      host="localhost",
      port="5432"
    )
  except Exception as e:
    return None

def connect_to_db():
  conn = get_connection()
  if conn is not None:
    print("Connection successful!")
    return conn
  else:  print("Connection failed.")

def close_connection(conn):
  if conn is not None:
    conn.close()
    print("Connection closed.")
  else: print("No connection to close.")

def create_cursor(conn):
  if conn is not None:
    return conn.cursor()
  else: print("No connection available to create a cursor.")

def make_commit(conn):
  if conn is not None:
    conn.commit()
    print("Changes committed to the database.")
  else: print("No connection available to commit changes.")

def create_tables(curr, queries):
  for query in queries:
    curr.execute(query)
  print("Tables created successfully.")

def insert_data(curr, query, dados):
  curr.execute(query, dados)
  print("Data inserted successfully.")

#%%
queries = [
  "CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, nome TEXT, email TEXT);",
  "CREATE TABLE IF NOT EXISTS produtos (id SERIAL PRIMARY KEY, nome TEXT, preco NUMERIC);",
  "CREATE TABLE IF NOT EXISTS pedidos (id SERIAL PRIMARY KEY, cliente_id INTEGER REFERENCES clientes(id), produto_id INTEGER REFERENCES produtos(id), quantidade INTEGER);"
]

clientes_data = [
  ("Alice", "alice@example.com"),
  ("Bob", "bob@example.com"),]

produtos_data = [
  ("Mouse", 25.99),
  ("Teclado", 45.50),
  ("Cadeira", 200.00),]

#%%
insert_clientes  = """INSERT INTO clientes(nome, email)
VALUES(%s, %s) RETURNING id;"""

insert_produtos = """INSERT INTO produtos(nome, preco)
VALUES(%s, %s) RETURNING id;"""

insert_pedidos = """INSERT INTO pedidos(cliente_id, produto_id, quantidade)
VALUES(%s, %s, %s);"""

# %%
conn = connect_to_db()
curr = create_cursor(conn)

#%%

try:
  create_tables(curr, queries)
  make_commit(conn)
except Exception as e:
  print(f"Error creating tables: {e}")
  conn.rollback()

#%%

clientes_ids ={}
produtos_ids = {}

try:
  for cliente in clientes_data:
    insert_data(curr, insert_clientes, cliente)
    cliente_id = curr.fetchone()[0]
    clientes_ids[cliente[0]] = cliente_id


  for produto in produtos_data:
    insert_data(curr, insert_produtos, produto)
    produto_id = curr.fetchone()[0]
    produtos_ids[produto[0]] = produto_id
  make_commit(conn)
except Exception as e:
  print(f"Error inserting data: {e}")
  conn.rollback()

#%%

pedidos_data = [
  (clientes_ids["Alice"], produtos_ids["Mouse"], 2),
  (clientes_ids["Bob"], produtos_ids["Teclado"], 1),
  (clientes_ids["Alice"], produtos_ids["Cadeira"], 1),]

try:
  for pedido in pedidos_data:
    insert_data(curr, insert_pedidos, pedido)
  make_commit(conn)
except Exception as e:
  print(f"Error inserting data: {e}")
  conn.rollback()


#%%
curr.execute("""
  SELECT table_name 
  FROM information_schema.tables 
  WHERE table_schema = 'public'
""")

tables = curr.fetchall()
for table in tables:
  print(table[0])


# %%
close_connection(conn)
curr.close()
# %%
