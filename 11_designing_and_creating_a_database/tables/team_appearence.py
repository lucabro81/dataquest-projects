import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS team_appearence
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS team_appearence (
            appearence_id INTEGER PRIMARY KEY,
            team_id TEXT,

            FOREIGN KEY(team_id) REFERENCES team(team_id)
        ) 
    ''')

def feed_table():
    db.run_command('''
        INSERT OR IGNORE INTO team_appearence(appearence_id, team_id)
        SELECT 
            p.appearance_id,
            CASE 
                WHEN p.person_id IN 
                (
                    v_manager_id, 
                    v_starting_pitcher_id, 
                    v_player_1_id, 
                    v_player_2_id, 
                    v_player_3_id, 
                    v_player_4_id, 
                    v_player_5_id,
                    v_player_6_id, 
                    v_player_7_id, 
                    v_player_8_id, 
                    v_player_9_id
                ) 
                THEN g.v_name
                ELSE g.h_name
            END AS team_id
        FROM person_appearance p
        INNER JOIN game_log g ON g.game_id == p.game_id
        WHERE appearance_type_id NOT IN ('UHP', 'U1B', 'U2B', 'U3B', 'ULF', 'URF', 'AWP', 'ALP', 'ASP', 'AWB')
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM team_appearence
    ''')
    print(result.shape);
    return result if num is None else result.head(num)