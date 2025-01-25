import pandas as pd
import os
import json

# Loads configuration settings
with open("config.json", "r") as file:
    config = json.load(file)

# Gets folder paths from configuration (config.json)
raw_data_folder = config["raw_data_folder"]
processed_data_folder = config["processed_data_folder"]

# Makes sure processed data folder exists
if not os.path.exists(processed_data_folder):
    os.makedirs(processed_data_folder)

# Processes each dataset for configuration
for dataset in config["AUTDProjectFiles"]:
    input_file = os.path.join(raw_data_folder, dataset["input_file"])
    output_file = os.path.join(processed_data_folder, dataset["output_file"])

    try:
        print(f"Processing {input_file}...")
        
        """
        Handles duplicate records, missing values left as null for better accuracy in future analysis. 
        Removes dollar signs where needed and reformats date so it can be read in SQL.
        """

        df = pd.read_csv(input_file)

        if 'Time' in df.columns:
            df['Time'] = df['Time'].str.replace(r'\s*EDT$', '', regex=True)

        # Addresses monetary columns and removes $ signs and commas
        monetary_cols = [col for col in df.columns if df[col].astype(str).str.contains('\$').any()]
        for col in monetary_cols:
            df[col] = df[col].replace({'\$': '', ',': ''}, regex=True).astype(float)

        df = df.drop_duplicates()
        df.to_csv(output_file, index=False)
        print(f"Processed data saved to {output_file}\n")


    # Handles errors and leaves message for reasoning behind error.
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please ensure this file exists in the raw data folder.\n")
    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}\n")