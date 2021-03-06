# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

#ongplays - records in log data associated with song plays i.e. records with page NextSong
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(songplay_id serial PRIMARY KEY NOT NULL,
                                     start_time bigint NULL, 
                                     user_id int NULL,
                                     level varchar NULL,
                                     song_id varchar NULL,
                                     artist_id varchar NULL,
                                     session_id int NULL,
                                     location varchar NULL,
                                     user_agent varchar NULL)
                        """)
#user_id, first_name, last_name, gender, level
user_table_create = ("""CREATE TABLE IF NOT EXISTS  users(user_id int PRIMARY KEY NOT NULL, 
                                                          first_name varchar NULL, 
                                                          last_name varchar NULL, 
                                                          gender varchar NULL, 
                                                          level varchar NULL)
""")

#song_id, title, artist_id, year, duration
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY NOT NULL, 
                                                         title varchar NULL, 
                                                         artist_id varchar NULL, 
                                                         year int NULL, 
                                                         duration decimal NULL)
""")

#artist_id, name, location, latitude, longitude
artist_table_create = ("""CREATE TABLE IF NOT EXISTS  artists(artist_id varchar PRIMARY KEY NOT NULL, 
                                                              name varchar NULL, 
                                                              location varchar NULL, 
                                                              latitude decimal NULL, 
                                                              longitude decimal NULL)
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (  start_time timestamp PRIMARY KEY NOT NULL, 
                                        hour int NULL, 
                                        day int NULL, 
                                        week int NULL, 
                                        month int NULL, 
                                        year int NULL, 
                                        weekday int NULL);
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s); 
""")

user_table_insert = (""" INSERT INTO users(user_id, first_name, last_name, gender, level) 
                         VALUES (%s,%s,%s,%s,%s) 
                         ON CONFLICT (user_id) 
                         DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = (""" INSERT INTO songs(song_id, title, artist_id, year, duration) 
                         VALUES (%s,%s,%s,%s,%s) 
                         ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = (""" INSERT INTO artists(artist_id, name, location, latitude, longitude) 
                           VALUES (%s,%s,%s,%s,%s) 
                           ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
song_select = (""" SELECT songs.song_id,artists.artist_id 
                   FROM songs 
                   JOIN artists
                   ON songs.artist_id = artists.artist_id 
                   WHERE songs.title=(%s) AND artists.name=(%s) and songs.duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
