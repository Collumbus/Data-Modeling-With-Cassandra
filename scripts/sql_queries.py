# DROP TABLES
artist_songs_table_drop = "DROP TABLE IF EXISTS artist_songs"
user_songs_table_drop = "DROP TABLE IF EXISTS user_songs"
listened_songs_table_drop = "DROP TABLE IF EXISTS listened_songs"

# CREATE TABLES
artist_songs_table_create = (
    """
        CREATE TABLE IF NOT EXISTS artist_songs (
            session_id INT,
            item_in_session INT,
            artist_name TEXT, 
            song_title TEXT,
            song_lengh FLOAT,
            PRIMARY KEY (session_id, item_in_session)
            )
    """)

user_songs_table_create = (
    """
        CREATE TABLE IF NOT EXISTS user_songs (
                user_id INT,
                session_id INT,
                item_in_session INT,
                artist_name TEXT, 
                song_title TEXT,
                first_name TEXT,
                last_name TEXT,
                PRIMARY KEY ((user_id, session_id), item_in_session)    
                )
    """)

listened_songs_table_create = (
    """
        CREATE TABLE IF NOT EXISTS listened_songs (
                song_title TEXT,
                user_id INT,
                first_name TEXT,
                last_name TEXT,
                PRIMARY KEY (song_title, user_id)    
                )
    """)

# INSERT RECORDS
artist_songs_table_insert = ("""
    INSERT INTO artist_songs (session_id, item_in_session, artist_name, song_title, song_lengh)
    VALUES (%s, %s, %s, %s, %s)
""")

user_songs_table_insert = ("""
    INSERT INTO user_songs (user_id, session_id, item_in_session, artist_name, song_title, first_name, last_name)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

listened_songs_table_insert = ("""
    INSERT INTO listened_songs (song_title, user_id, first_name, last_name)
    VALUES (%s, %s, %s, %s)
""")

# Queries
query_1 = ("""
    SELECT 
            artist_name, 
            song_title, 
            song_lengh 
    FROM artist_songs 
    WHERE session_id = 338 AND item_in_session = 4
""")

query_2 = ("""
    SELECT 
            artist_name, 
            song_title, 
            first_name, 
            last_name 
            FROM user_songs 
            WHERE user_id = 10 AND session_id = 182
""")

query_3 = ("""
    SELECT 
            first_name, 
            last_name 
    FROM listened_songs 
    WHERE song_title = 'All Hands Against His Own'
""")

# QUERY LISTS
create_table_queries = [artist_songs_table_create, user_songs_table_create, listened_songs_table_create]
drop_table_queries = [artist_songs_table_drop, user_songs_table_drop, listened_songs_table_drop]
insert_table_queries = [artist_songs_table_insert, user_songs_table_drop, listened_songs_table_insert]
queries = [query_1, query_2, query_3]
queries_title = ["Q1: Give the artist, song title and song's length in the music app history that was heard during "
                 "sessionId = 338, and itemInSession = 4",
                 "Q2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and "
                 "last name) for userid = 10, sessionid = 182",
                 "Q3: Give every user name (first and last) in my music app history who listened to the song 'All "
                 "Hands Against His Own'"]