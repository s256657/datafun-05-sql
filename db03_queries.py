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

            # Execute the SELECT query to get books published after 1950
            cursor.execute("SELECT * FROM books WHERE year_published > 1950")
            
            # Fetch all rows matching the query
            rows = cursor.fetchall()

            if rows:
                print("Books published after 1950:")
                for row in rows:
                    print(row)  # Print each book's details (each row is a tuple)
            else:
                print("No books found published after 1950.")
            
            # Execute the SELECT query with GROUP BY for the year ranges
            cursor.execute("""
                SELECT
                    CASE
                        WHEN year_published < 1930 THEN 'Before 1930'
                        WHEN year_published BETWEEN 1931 AND 1940 THEN '1931-1940'
                        WHEN year_published BETWEEN 1941 AND 1950 THEN '1941-1950'
                        WHEN year_published > 1950 THEN 'After 1950'
                    END AS year_range,
                    COUNT(*) AS books_count
                FROM books
                GROUP BY year_range
                ORDER BY year_range;
            """)

            # Fetch all rows matching the query
            rows = cursor.fetchall()

            if rows:
                print("Books grouped by publication year:")
                for row in rows:
                    print(f"{row[0]}: {row[1]} books")
            else:
                print("No books found.")

    except sqlite3.Error as e:
        print("Error executing query:", e)


def main():
    perform_aggregations()

if __name__ == "__main__":
    main()