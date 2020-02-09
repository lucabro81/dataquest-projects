import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS park
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS park (
            park_id TEXT PRIMARY KEY,
            city_id INTEGER,
            league_id TEXT,
            name TEXT,
            aka TEXT,
            notes TEXT,

            FOREIGN KEY(city_id) REFERENCES city(city_id),
            FOREIGN KEY(league_id) REFERENCES league(league_id)
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO park(
            park_id,
            city_id,
            league_id,
            name,
            aka,
            notes
        )
        SELECT p.park_id, c.city_id, l.league_id, p.name, p.aka, p.notes
        FROM park_codes p
        LEFT JOIN city c ON p.city == c.name
        LEFT JOIN league l ON p.league == l.league_id
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM park
    ''')
    print(result.shape);
    return result if num is None else result.head(num)