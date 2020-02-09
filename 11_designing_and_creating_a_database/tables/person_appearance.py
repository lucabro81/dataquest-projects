import utils.db as db

def drop_table():
    db.run_command('''
        DROP TABLE IF EXISTS person_appearance
    ''')

def create_table():
    db.run_command('''
        CREATE TABLE IF NOT EXISTS person_appearance (
            appearance_id INTEGER PRIMARY KEY,
            game_id TEXT,
            person_id TEXT,
            appearance_type_id TEXT,

            FOREIGN KEY(game_id) REFERENCES game(game_id),
            FOREIGN KEY(person_id) REFERENCES person(person_id)
        ) 
    ''')

def feed_table():
    # yes, copied from solution...
    c2 = """
        INSERT OR IGNORE INTO person_appearance (
            game_id,
            person_id,
            appearance_type_id
        ) 
            SELECT
                game_id,
                hp_umpire_id,
                "UHP"
            FROM game_log
            WHERE hp_umpire_id IS NOT NULL    

        UNION

            SELECT
                game_id,
                [1b_umpire_id],
                "U1B"
            FROM game_log
            WHERE "1b_umpire_id" IS NOT NULL

        UNION

            SELECT
                game_id,
                [2b_umpire_id],
                "U2B"
            FROM game_log
            WHERE [2b_umpire_id] IS NOT NULL

        UNION

            SELECT
                game_id,
                [3b_umpire_id],
                "U3B"
            FROM game_log
            WHERE [3b_umpire_id] IS NOT NULL

        UNION

            SELECT
                game_id,
                lf_umpire_id,
                "ULF"
            FROM game_log
            WHERE lf_umpire_id IS NOT NULL

        UNION

            SELECT
                game_id,
                rf_umpire_id,
                "URF"
            FROM game_log
            WHERE rf_umpire_id IS NOT NULL

        UNION

            SELECT
                game_id,
                v_manager_id,
                "MM"
            FROM game_log
            WHERE v_manager_id IS NOT NULL

        UNION

            SELECT
                game_id,
                h_manager_id,
                "MM"
            FROM game_log
            WHERE h_manager_id IS NOT NULL

        UNION

            SELECT
                game_id,
                winning_pitcher_id,
                "AWP"
            FROM game_log
            WHERE winning_pitcher_id IS NOT NULL

        UNION

            SELECT
                game_id,
                losing_pitcher_id,
                "ALP"
            FROM game_log
            WHERE losing_pitcher_id IS NOT NULL

        UNION

            SELECT
                game_id,
                saving_pitcher_id,
                "ASP"
            FROM game_log
            WHERE saving_pitcher_id IS NOT NULL

        UNION

            SELECT
                game_id,
                winning_rbi_batter_id,
                "AWB"
            FROM game_log
            WHERE winning_rbi_batter_id IS NOT NULL

        UNION

            SELECT
                game_id,
                v_starting_pitcher_id,
                "PSP"
            FROM game_log
            WHERE v_starting_pitcher_id IS NOT NULL

        UNION

            SELECT
                game_id,
                h_starting_pitcher_id,
                "PSP"
            FROM game_log
            WHERE h_starting_pitcher_id IS NOT NULL;
    """

    template = """
        INSERT OR IGNORE INTO person_appearance (
            game_id,
            person_id,
            appearance_type_id
        ) 
            SELECT
                game_id,
                {hv}_player_{num}_id,
                "O{num}"
            FROM game_log
            WHERE {hv}_player_{num}_id IS NOT NULL

        UNION

            SELECT
                game_id,
                {hv}_player_{num}_id,
                "D" || CAST({hv}_player_{num}_def_pos AS INT)
            FROM game_log
            WHERE {hv}_player_{num}_id IS NOT NULL;
    """

    db.run_command(c2)

    for hv in ["h","v"]:
        for num in range(1,10):
            query_vars = {
                "hv": hv,
                "num": num
            }
            db.run_command(template.format(**query_vars))

def show_table(num):
    result = db.run_query(f'''
        SELECT * FROM person_appearance
    ''')
    print(result.shape);
    return result if num is None else result.head(num)