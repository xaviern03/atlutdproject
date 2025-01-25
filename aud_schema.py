import sqlite3

connect = sqlite3.connect("aud_project_data.db")

connect.close()

print("Database created successfully.")