# datafun-05-sql

## Purpose

This project is to begin integrating Python and SQL using SQLite.
Skills used will be creating and managing a database, building a schema, and performing various SQL operations including queries with joins, filters, and aggregations.

## Commands to run script project
Below are the following commands in order to run the project as designed. Details in created the project follow.

1. To initialize and create tables
``` python3 db01_setup.py ```


The following steps is how I created this project using VSCode on macOS. Depending on tools you are using steps could be slightly different

## Step 1: Create project and add basic requirements

1. Create repo named datafun-05-sql in github 
2. Clone down to local machine
3. Added .gitignore, requirements.txt, and utils_logger.py
- files are in this repository and can be copied into the file
4. Create virtual environment
```
python3 -m venv .venv
```

## Step 2: First Iteration
This step activated required items and created folders to organize and prepare for the duration of the project

1. Activate virtual environment
```
source .venv/bin/activate
```
2. Install dependencies
```
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
```
- Note: based on my version of python I changed sqlite3 to read only as an error occured because python already had sqlite3 installed.
```
python3 utils_logger.py
```
3. Organized project by creating folders and subfolders
- sql_create: 01_drop_tables.sql, 02_create_tables.sql, 03_insert_tables.sql, db01_setup.py
- sql_features: update_records.sql, delete_records.sql, 
- sql_queries: query_aggregation.sql, query_filter.sql, query_group_by.sql, query_join.sql, query_sorting.sql, db03_queries.py

## Step 3: Create simple database with two related tables
1. Create folder "data" then two subfolders named "authors.csv" and "books.csv"
2. Data to be added in authors.csv
```
author_id,first,last
10f88232-1ae7-4d88-a6a2-dfcebb22a596,Harper,Lee
c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70,George,Orwell
e0b75863-866d-4db4-85c7-df9bb8ee6dab,F. Scott,Fitzgerald
7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d,Aldous,Huxley
8d8107b6-1f24-481c-8a21-7d72b13b59b5,J.D.,Salinger
0cc3c8e4-e0c0-482f-b2f7-af87330de214,Ray,Bradbury
4dca0632-2c53-490c-99d5-4f6d41e56c0e,Jane,Austen
16f3e0a1-24cb-4ed6-a50d-509f63e367f7,J.R.R.,Tolkien
06cf58ab-90f1-448d-8e54-055e4393e75c,J.R.R.,Tolkien
6b693b96-394a-4a1d-a4e2-792a47d7a568,J.K.,Rowling
```
3. Data to be added in books.csv
```
book_id,title,year_published,author_id
d6f83870-ff21-4a5d-90ab-26a49ab6ed12,To Kill a Mockingbird,1960,10f88232-1ae7-4d88-a6a2-dfcebb22a596
0f5f44f7-44d8-4f49-b8c4-c64d847587d3,1984,1949,c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70
f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2,The Great Gatsby,1925,e0b75863-866d-4db4-85c7-df9bb8ee6dab
38e530f1-228f-4d6e-a587-2ed4d6c44e9c,Brave New World,1932,7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d
c2a62a4b-cf5c-4246-9bf7-b2601d542e6d,The Catcher in the Rye,1951,8d8107b6-1f24-481c-8a21-7d72b13b59b5
3a1d835c-1e15-4a48-8e8c-b12239604e98,Fahrenheit 451,1953,0cc3c8e4-e0c0-482f-b2f7-af87330de214
c6e67918-e509-4a6b-bc3a-979f6ad802f0,Pride and Prejudice,1813,4dca0632-2c53-490c-99d5-4f6d41e56c0e
be951205-6cc2-4b3d-96f1-7257b8fc8c0f,The Hobbit,1937,16f3e0a1-24cb-4ed6-a50d-509f63e367f7
dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f,The Lord of the Rings,1954,06cf58ab-90f1-448d-8e54-055e4393e75c
ca8e64c3-1e67-47f5-82cc-3e4e30f63b75,Harry Potter and the Philosopher's Stone,1997,6b693b96-394a-4a1d-a4e2-792a47d7a568
```

## Step 4: Initialize Data Base
This step utilizes sql_create folder and db01_setup.py to complete. 

1. Add code to 01_drop_tables.sql, 02_create_tables.sql, and 03_insert_records.sql
2. Add code to db01_setup.py as this is what will run to initialize the database
- Order is important must drop first or create tables will not run properly
3. An SQL viewer is required to see the final product
- If using VS Code search and install SQLite Viewer
- (optional) another SQL viewer can be used but the SQLite Viewer within VSCode is simple to install and run