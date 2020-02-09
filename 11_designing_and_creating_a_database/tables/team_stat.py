import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS team_stat
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS team_stat (
            game_id TEXT PRIMARY KEY,
            team_id TEXT,
            game_number INTEGER, 
            score INTEGER, 
            line_score TEXT, 
            at_bats INTEGER, 
            hits INTEGER, 
            doubles INTEGER,  
            triples INTEGER, 
            homeruns INTEGER, 
            rbi INTEGER, 
            sacrifice_hits INTEGER,  
            sacrifice_flies INTEGER, 
            hit_by_pitch INTEGER, 
            walks INTEGER,  
            intentional_walks INTEGER, 
            strikeouts INTEGER,  
            stolen_bases INTEGER, 
            caught_stealing INTEGER, 
            grounded_into_double INTEGER, 
            first_catcher_interference INTEGER,  
            left_on_base INTEGER, 
            pitchers_used INTEGER, 
            individual_earned_runs INTEGER, 
            team_earned_runs INTEGER, 
            wild_pitches INTEGER, 
            balks INTEGER, 
            putouts INTEGER,  
            assists INTEGER, 
            errors INTEGER, 
            passed_balls INTEGER, 
            double_plays INTEGER,  
            triple_plays INTEGER,

            FOREIGN KEY(team_id) REFERENCES team(team_id)
        )
    ''')

def feed_table():
    columns = [
        "game_number" , 
        "score" , 
        "line_score" , 
        "at_bats" , 
        "hits" , 
        "doubles" ,  
        "triples" , 
        "homeruns" , 
        "rbi" , 
        "sacrifice_hits" ,  
        "sacrifice_flies" , 
        "hit_by_pitch" , 
        "walks" ,  
        "intentional_walks" , 
        "strikeouts" ,  
        "stolen_bases" , 
        "caught_stealing" , 
        "grounded_into_double" , 
        "first_catcher_interference" ,  
        "left_on_base" , 
        "pitchers_used" , 
        "individual_earned_runs" , 
        "team_earned_runs" , 
        "wild_pitches" , 
        "balks" , 
        "putouts" ,  
        "assists" , 
        "errors" , 
        "passed_balls" , 
        "double_plays" ,  
        "triple_plays"
    ]

    db.run_command(f'''
        INSERT OR IGNORE INTO team_stat(game_id, team_id, {','.join([f'{c}' for c in columns])})
        SELECT game_id, team_id, {','.join([f'{c}' for c in columns])} 
        FROM (
            SELECT 
                game_id, v_name team_id, {','.join([f'v_{c} {c}' for c in columns])}, date
            FROM game_log
            UNION
            SELECT 
                game_id, h_name team_id, {','.join([f'h_{c} {c}' for c in columns])}, date
            FROM game_log
            ORDER BY date
        )
    ''')

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM team_stat
    ''')
    print(result.shape);
    return result if num is None else result.head(num)