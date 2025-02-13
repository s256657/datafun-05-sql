import sqlite3
import pathlib

# Script to run sql_features to delete records and update records

db_file = pathlib.Path("project.sqlite3")

def delete_record():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "delete_records.sql")
            if not sql_file.exists():
                print(f"SQL file not found: {sql_file}")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Record deleted successfully")
    except sqlite3.Error as e:
        print("Error deleting records", e)

def update_record():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_features", "update_records.sql")
            if not sql_file.exists():
                print(f"SQL file not found: {sql_file}")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Record updated successfully")
    except sqlite3.Error as e:
        print("Error updating records", e)

def main():
    delete_record()
    update_record()

if __name__ == "__main__":
    main()
