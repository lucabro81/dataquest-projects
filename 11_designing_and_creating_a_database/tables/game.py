import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS game
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS game (
            game_id TEXT PRIMARY KEY,
            park_id TEXT,
            date DATE,
            number_of_game VARCHAR(1),
            length_outs INTEGER,
            day BOOLEAN,
            completion TEXT,
            forefeit VARCHAR(1),
            protest VARCHAR(1),
            attendance INTEGER,
            length_minutes INTEGER,
            additional_info TEXT,
            acquisition_info VARCHAR(1),

            FOREIGN KEY(park_id) REFERENCES park(park_id)
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO game
        SELECT 
            game_id,
            park_id,
            date,
            number_of_game,
            length_outs,
            CASE 
                WHEN day_night=='D' 
                    THEN TRUE 
                WHEN day_night=='N'
                    THEN FALSE
                ELSE NULL END AS day,
            completion,
            forefeit,
            protest,
            attendance,
            length_minutes,
            additional_info,
            acquisition_info
        FROM game_log
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM game
    ''')
    print(result.shape);
    return result if num is None else result.head(num)