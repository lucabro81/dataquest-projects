import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS person
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS person (
            person_id TEXT PRIMARY KEY,
            first TEXT,
            last TEXT
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO person
        SELECT id, first, last
        FROM person_codes
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM person
    ''')
    print(result.shape);
    return result if num is None else result.head(num)