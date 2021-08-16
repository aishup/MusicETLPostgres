Improve the Introduction with the purpose of the project, what is Sparkify, how the ETL is going to work.
Add the Database schema design with the tables and the columns
Add a section on how to run the Python scripts

Project Summary:

A startup company named "Sparkify" wants to analyse on the data collected in their music streaming app. They want to analyse the user activity and the songs listened by the users.As data engineers, this project is implemented by Data Modelling using Postgres and ETL Pipeline build using python.

ETL Process:
ETL means Extract, Transform and load. The data is extracted from the song and log files in JSON File format, transformed into a two dimensional datastructure using pandas dataframe and then data loaded in star schema datamart i.e the single fact table and multiple dimension table around the fact table.

Star Database Schema:
Tables:
- Dimension Tables:
  -> Table users 
        - Extracted the columns user_id(primary key),first_name,last_name,gender,level from "log file"
  -> song 
        - Extracted the columns song_id(primary key),title,artist_id,year,duration from "song file"
  -> artists
        - Extracted the columns artist_id(primary key),name,location,latitude,longtitude from "song file"
  -> time 
        - Extracted the columns start_time(primary key),hour,day,week,month,year,weekday from "log file"

- Fact table 
  -> Songplays
        - Extracted the song play_id,user_id,level,session_id,location,user_agent from "log file" for the rows having "Next Song"
        - Extracted song_id,artist_id from song ,artists table respectively based on the title, artist name, and duration of a song.
        - Extracted the start_time from time table

   
Execution of Python Scripts:
  1. Using the command "Python3 create_tables.py" is run the python files.  
  
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

