import sqlite3
import pathlib
import pandas as pd

# Script to run sql_queries

db_file = pathlib.Path("project.sqlite3")

def perform_aggregations():
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()

            # Running a SELECT query to get all rows from the books table
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()  # This fetches all the rows from the query

            print("Books in the database:")
            for row in rows:
                print(row)  # Print each row
            
            # Example of getting the count of books
            cursor.execute("SELECT COUNT(*) FROM books")
            count_result = cursor.fetchone()[0]
            print(f"\nTotal number of books: {count_result}")

            # Get the first (earliest) published book year
            cursor.execute("SELECT MIN(year_published) FROM books")
            first_published = cursor.fetchone()[0]
            print(f"First published book year: {first_published}")

            # Get the last (latest) published book year
            cursor.execute("SELECT MAX(year_published) FROM books")
            last_published = cursor.fetchone()[0]
            print(f"Last published book year: {last_published}")

    except sqlite3.Error as e:
        print("Error in aggregations:", e)

def main():
    perform_aggregations()

if __name__ == "__main__":
    main()