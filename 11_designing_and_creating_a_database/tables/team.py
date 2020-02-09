import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS team
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS team (
            team_id TEXT PRIMARY KEY,
            league_id TEXT,
            city_id INTEGER,
            nickname TEXT,
            french_id TEXT,
            seq INTEGER,

            FOREIGN KEY(league_id) REFERENCES league(league_id),
            FOREIGN KEY(city_id) REFERENCES city(city_id)
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO team(
            team_id,
            league_id,
            city_id,
            nickname,
            french_id,
            seq
        )
        SELECT 
            t.team_id, 
            t.league, 
            c.city_id, 
            t.nickname, 
            t.franch_id,
            t.seq
        FROM team_codes t
        LEFT JOIN city c ON c.name == t.city
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM team
    ''')
    print(result.shape);
    return result if num is None else result.head(num)