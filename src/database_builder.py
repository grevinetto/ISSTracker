import sqlite3, os

""" 
Ideally, this code should provide a starting point to create an automated Python script
that runs from time to time and stores the ISS position for further analysis
"""

# Create the SQLite3 database which will store the ISS latitudes and longitudes
    
def create_db():

    # Define in which directory the .db file with the ISS latitude and longitude will be stored
    # In this case, it will be saved in the data folder in the parent directory of src
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, '../data/'))
    db_path = os.path.join(parent_directory, "iss_positions.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            latitude REAL,
            longitude REAL
        )
    ''')

    conn.commit()
    conn.close()

    return db_path
    
# Store the ISS position (latitude and longitude) in a SQLite database

def insert_lat_and_lng(db_path, latitude, longitude):
    if not latitude or not longitude:
        return

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO positions (timestamp, latitude, longitude) VALUES (CURRENT_TIMESTAMP, ?, ?)",
                   (latitude, longitude))

    conn.commit()
    conn.close()


# Retrieve the data from the .db file

def fetch_data_from_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT timestamp, latitude, longitude FROM positions")
    data = cursor.fetchall()

    conn.close()
    return data

# Convert the data from the .db file to a Python dictionary

def convert_to_dictionary(data):
    columns = ['timestamp', 'latitude', 'longitude']
    result = []

    for row in data:
        row_dict = dict(zip(columns, row))
        result.append(row_dict)

    return result


