import sqlite3
import pandas as pd

db_name = 'mlb.db'

def set_db_name(name):
    db_name = name

def import_table(df, table_name):
    with sqlite3.connect(db_name) as conn:
        df.to_sql(table_name, conn, index=False, if_exists='replace')

def run_query(q):
    with sqlite3.connect(db_name) as conn:
        return pd.read_sql(q, conn)
    
def create_function(name, func):
    with sqlite3.connect(db_name) as conn:
        conn.create_function(name, len(signature(run_query).parameters), func)
    
def run_command(c):
    with sqlite3.connect(db_name) as conn:
        conn.isolation_level = None
        conn.execute(c)