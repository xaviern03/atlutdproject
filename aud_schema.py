import sqlite3

connect = sqlite3.connect("aud_project_data.db")
cursor = connect.cursor()

create_match_data_table = """
CREATE TABLE IF NOT EXISTS match_data (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_date TEXT,
    game_time TEXT,
    home_team TEXT,
    h_goals INTEGER,
    h_xg REAL,
    hplayer_xg REAL,
    away_team TEXT,
    a_goals INTEGER,
    a_xg REAL,
    aplayer_xg REAL,
    goal_diff INTEGER,
    x_gd REAL,
    player_xgd REAL,
    final_diff INTEGER,
    h_xpoints REAL,
    a_xpoints REAL
);
"""

create_salary_data_table = """
CREATE TABLE IF NOT EXISTS salary_data (
    player TEXT,
    team TEXT,
    season INTEGER,
    position TEXT,
    base_salary REAL,
    guaranteed REAL,
    date TEXT

);
"""


