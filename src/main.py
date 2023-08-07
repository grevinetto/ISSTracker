from api_interaction import retrieve_iss_position
from database_builder import create_db, insert_lat_and_lng, fetch_data_from_database, convert_to_dictionary
from map_plotter import world_map_plotter
""""
A small snippet of code that shows expected functionality 
(retrieve a list of Python dictionaries from the SQLite db that can be manipulated)
"""

def main():
    # SQLite3 database creation
    path_to_db = create_db()

    # Retrieve ISS position (latitude and longitude)
    json_data = retrieve_iss_position()

    if json_data:

        # Store ISS positions on database
        insert_lat_and_lng(path_to_db, *json_data)

        # Retrieve the data from database
        data = fetch_data_from_database(path_to_db)

        # Convert the data into a list of Python dictionaries
        result = convert_to_dictionary(data)

        # Plot ISS position on world map
        print(result[0]["latitude"], result[0]["longitude"])
        world_map_plotter(result[0]["latitude"], result[0]["longitude"])


if __name__ == "__main__":
    main()   