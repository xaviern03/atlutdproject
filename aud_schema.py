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

create_player_goal_data = """
CREATE TABLE IF NOT EXISTS player_goal_data (
    player_id INTEGER,
    player TEXT,
    team TEXT,
    season INTEGER,
    position TEXT,
    minutes INTEGER,
    dribbling REAL,
    fouling REAL,
    interrupting REAL,
    passing REAL,
    receiving REAL,
    shooting REAL,
    goals_added REAL,
    PRIMARY KEY (player_id, season, team)
);
"""
create_player_pass_data = """
CREATE TABLE IF NOT EXISTS player_pass_data (
    player_id INTEGER PRIMARY KEY,
    player TEXT,
    team TEXT,
    season INTEGER,
    position TEXT,
    minutes INTEGER,
    passes INTEGER,
    pass_percent REAL,
    xpass_percent REAL,
    pass_score REAL,
    p_score_per_100 REAL,
    avg_distance REAL,
    avg_pass_vert REAL,
    touch_perc REAL,
    games_played INTEGER,
    PRIMARY KEY (player_id, season, team) 

);
"""


