import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS city
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS city (
            city_id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO city(name, state)
        SELECT city, state
        FROM park_codes
        GROUP BY city, state;
    ''')

def show_table(num):
    result = db.run_query('''
        SELECT * FROM city
    ''')
    print(result.shape);
    return result if num is None else result.head(num)