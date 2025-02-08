# datafun-05-sql

## Purpose

This project is to begin integrating Python and SQL using SQLite.
Skills used will be creating and managing a database, building a schema, and performing various SQL operations including queries with joins, filters, and aggregations.

The following steps is how I created this project using VSCode on macOS. Depending on tools you are using steps could be slightly different

## Step 1: Create project and add basic requirements

1. Create repo named datafun-05-sql in github 
2. Clone down to local machine
3. Added .gitignore, requirements.txt, and utils_logger.py
- files are in this repository and can be copied into the file
4. Create virtual environment
'''
python3 -m venv .venv
'''

## Step 2: First Iteration
This step activated required items and created folders to organize and prepare for the duration of the project

1. Activate virtual environment
'''
source .venv/bin/activate
'''
2. Install dependencies
'''
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
'''
- Note: based on my version of python I changed sqlite3 to read only as an error occured because python already had sqlite3 installed.
'''
python3 utils_logger.py
'''
3. Organized project by creating folders and subfolders
- sql_create: 01_drop_tables.sql, 02_create_tables.sql, 03_insert_tables.sql, db01_setup.py
- sql_features: update_records.sql, delete_records.sql, 
- sql_queries: query_aggregation.sql, query_filter.sql, query_group_by.sql, query_join.sql, query_sorting.sql, db03_queries.py

------ To Be Continued