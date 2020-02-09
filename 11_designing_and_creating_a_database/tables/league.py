import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS league
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS league (
            league_id TEXT,
            name TEXT
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO league(league_id, name)
        VALUES
            ('NL', 'National League'),
            ('AL', 'American League'),
            ('FL', 'Federal League'),
            ('PL', "Players' League"),
            ('UA', 'Union Association'),
            ('AA', 'American Association')
    ''')

def show_table(num=None):
    result = db.run_query('''
        SELECT * FROM league
    ''')
    print(result.shape)
    return result if num is None else result.head(num)