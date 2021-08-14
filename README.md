
Project Summary:

This project is an example on how to implement Data Modelling wih Postgres and build an ETL Pipeline using python. Data is extracted from the JSON File format , transformed into a two dimensional datastructure using pandas dataframe and then ,loaded into the fact and dimension tables in the star schema. 

Files of the Project:

- create_tables.py : This python script file performs the below functions:
    1. Calls the local functions 'Drop' and 'Create' which will run the sql queries to drop and create new fact table(songplays) and dimension tables(time,users,songs,artists). 
    2. Sql queryies are imported from the python file sql_queries.py 
- sql_queries.py : This python sql drops the table if already present in the database, creates new tables and inserts the records.
- etl.ipynb : 
    1. This interactive jupter notebook file helps to execute the ETL process step by step to process a single record from the song and log files.
    2. After processing the first few records successfully, data is inserted into the respective tables. 
- etl.py : 
    1. After successfully processing, and inserting the single record, this ETL python file is executed via the terminal and entire file is processed. 
- test.ipynb : 
    1. This interactive python file run the select sql sequeries to check if the values are inserted into the db successfully.



