import pandas as pd
import os
import json

# Loads configuration settings
def load_config(file_path="config.json"):
    with open("config.json", "r") as file:
        return json.load(file)

#Clean specific columns
def clean_data(df):
    # Converts dates from MM/DD/YYYY to the standardized YYYY-MM-DD format for consistency if needed
    if 'Date' in df.columns:
        try:
            df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
        except ValueError:
            print("")

    # Address columns that have EDT at the end of the time   
    if 'Time' in df.columns:
        df['Time'] = df['Time'].str.replace(r'\s*EDT$', '', regex=True)

    # Addresses monetary columns and removes $ signs and commas
    monetary_cols = [col for col in df.columns if df[col].astype(str).str.contains('\$').any()]
    for col in monetary_cols:
        df[col] = df[col].replace({'\$': '', ',': ''}, regex=True).astype(float)

    # Clean percentage columns, removing % and converting to float
    percent_cols = [col for col in df.columns if df[col].astype(str).str.contains('%').any()]
    for col in percent_cols:
        df[col] = df[col].str.replace('%', '', regex=False).astype(float)

    #Drop duplicates and empty columns
    df = df.drop_duplicates()
    df = df.dropna(axis=1, how='all')
    
    return df

# Assign unique player IDs
def assign_player_ids(df, unique_players):
    new_players = {player: len(unique_players) + i + 1 for i, player in enumerate(df["Player"].unique()) if player not in unique_players}
    unique_players.update(new_players)
    df["player_id"] = df["Player"].map(unique_players)
    return df

# Process a single dataset
def process_dataset(input_file, output_file, unique_players):
    try:
        print(f"Processing {input_file}...")
        df = pd.read_csv(input_file)
        
    # Add unique player IDs
        if "Player" in df.columns:
            df = assign_player_ids(df, unique_players)
        
    # Clean the data
        df = clean_data(df)

    # Standardize column headers
        df.columns = [col.replace(" ", "_").replace(",", "_").replace("%", "_Percent") for col in df.columns]

    # Drop duplicates
        df = df.drop_duplicates()

    # Save to output
        df.to_csv(output_file, index=False)
        print(f"Processed data saved to {output_file}\n")
    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}\n")

# Ensure necessary folders exist
def ensure_directories(config):
    raw_data_folder = config["raw_data_folder"]
    processed_data_folder = config["processed_data_folder"]

    if not os.path.exists(processed_data_folder):
        os.makedirs(processed_data_folder)

    return raw_data_folder, processed_data_folder

if __name__ == "__main__":
    config = load_config()
    raw_data_folder, processed_data_folder = ensure_directories(config)
    unique_players = {}

    for dataset in config["AUTDProjectFiles"]:
        input_file = os.path.join(raw_data_folder, dataset["input_file"])
        output_file = os.path.join(processed_data_folder, dataset["output_file"])
        process_dataset(input_file, output_file, unique_players)