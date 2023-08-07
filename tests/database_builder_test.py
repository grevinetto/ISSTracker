import sys
sys.path.append("..")
import unittest
import sqlite3
import os

from src.database_builder import create_db, insert_lat_and_lng, fetch_data_from_database, convert_to_dictionary

class TestISSDatabase(unittest.TestCase):

    def setUp(self):
        # Create a temporary database for testing
        self.temp_db_path = 'test_iss_positions.db'
        self.db_conn = sqlite3.connect(self.temp_db_path)
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS positions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                latitude REAL,
                longitude REAL
            )
        ''')
        self.db_conn.commit()

    def test_create_db(self):
        db_path = create_db()
        self.assertTrue(os.path.exists(db_path))
        self.assertTrue(os.path.isfile(db_path))

    def test_insert_lat_and_lng(self):
        latitude = 40.7128
        longitude = -74.0060
        insert_lat_and_lng(self.temp_db_path, latitude, longitude)
        data = fetch_data_from_database(self.temp_db_path)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], latitude)
        self.assertEqual(data[0][2], longitude)

    def test_fetch_data_from_database(self):
        latitude1 = 40.7128
        longitude1 = -74.0060
        latitude2 = 34.0522
        longitude2 = -118.2437
        insert_lat_and_lng(self.temp_db_path, latitude1, longitude1)
        insert_lat_and_lng(self.temp_db_path, latitude2, longitude2)
        data = fetch_data_from_database(self.temp_db_path)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], latitude1)
        self.assertEqual(data[0][2], longitude1)
        self.assertEqual(data[1][1], latitude2)
        self.assertEqual(data[1][2], longitude2)

    def test_convert_to_dictionary(self):
        data = [('2023-08-07 12:34:56', 40.7128, -74.0060), ('2023-08-08 01:23:45', 34.0522, -118.2437)]
        result = convert_to_dictionary(data)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['timestamp'], '2023-08-07 12:34:56')
        self.assertEqual(result[0]['latitude'], 40.7128)
        self.assertEqual(result[0]['longitude'], -74.0060)
        self.assertEqual(result[1]['timestamp'], '2023-08-08 01:23:45')
        self.assertEqual(result[1]['latitude'], 34.0522)
        self.assertEqual(result[1]['longitude'], -118.2437)

    def tearDown(self):
        # Close the database connection and remove the temporary database
        self.db_conn.close()
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

        # Remove the original iss_positions.db file if it exists
        original_db_path = os.path.join('..', 'data', 'iss_positions.db')
        if os.path.exists(original_db_path):
            os.remove(original_db_path)

if __name__ == '__main__':
    unittest.main()

