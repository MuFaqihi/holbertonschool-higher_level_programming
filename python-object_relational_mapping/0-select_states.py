#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database using credentials from command-line arguments
    db = MySQLdb.connect(
        host="localhost",      # Host where the database server is running
        port=3306,             # Default MySQL port
        user=argv[1],          # Username passed as first argument
        passwd=argv[2],        # Password passed as second argument
        db=argv[3]             # Database name passed as third argument
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute a SQL query to select all rows from the 'states' table ordered by 'id'
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results returned by the query
    rows = cursor.fetchall()

    # Loop through the result set and print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection to free resources
    cursor.close()
    db.close()
