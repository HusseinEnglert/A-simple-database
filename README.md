# Book Database Management 

This Python script uses the `mysql.connector` library to create and manipulate tables in a MySQL database. The code exemplifies how to create tables, insert data, and perform queries using SQL in Python.

## Features

1. Table Creation: Creates a books table that stores information about books, such as name, author, publication year, and a foreign key publisher_id that relates to the publisher table.Creates a publisher table that stores the names of publishers.
2. Data Insertion: Inserts sample data into the books table.Inserts publisher names into the publisher table.
3. SQL Queries: Selects and displays books published before the year 2000.Performs a join (JOIN) between the books and publisher tables, displaying the book's name, author, and corresponding publisher.

## Prerequisites

- Python 3.x installed
- ``mysql.connector`` library installed
- A configured MySQL database

## How to Use

1. Clone this repository:
```bash
git clone https://github.com/HusseinEnglert/book-database-management.git
cd book-database-management
```
2. Install the required dependencies:
```bash
pip install mysql-connector-python
```
3. Configure the database connection:
 - Edit the following lines in the code to match your MySQL configuration:
```python 
con = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password=password,
    database='your_database',)
```
4. Run the script:
 - In the terminal, run the Python script:
`` python script_name.py``
5. Enter your MySQL password:
 - When prompted, enter the MySQL user password.

## Error Handling

If an error occurs during execution, the books and publisher tables will be automatically dropped to ensure that the database remains consistent.