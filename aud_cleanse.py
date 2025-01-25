import pandas as pd
import os
import json

with open("config.json", "r") as file:
    config = json.load(file)

raw_data_folder = config["raw_data_folder"]
processed_data_folder = config["processed_data_folder"]

if not os.path.exists(processed_data_folder):
    os.makedirs(processed_data_folder)