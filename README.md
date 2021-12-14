# Project: Data Modeling with Apache Cassandra
It is a project where I applied concepts data modelling with Apache Cassandra and built an ETL pipeline using Python. To complete the project has been defined a data model by creating tables in Apache Cassandra to run queries. I am provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

This project models user activity data for a music streaming app called Sparkify to optimize queries for understanding what songs users are listening to by using **Apache Cassandra**.

1. Build up ETL to iterate/process events raw dataset and generate new dataset
2. Creating appropriate Apache Cassandra tables to answer 3 specific questions
3. Inserting data from new dataset to Apache Cassandra tables
4. Testing the results by select statements


## Project Structure

```
Data Modeling with Cassandra
|____data                        # Dataset
| |____event_data                # Raw dataset  (csv files)
| |____event_datafile_new.csv    # New dataset by iterating event_data
|   |____...events.csv
|
|____jupyter_notebooks		 # Notebooks for developing and testing ETL
| |____etl_cassandra.ipynb       # Notebook for Apache Cassandra queries
|
|____scripts        		 # Python codes
| |____etl_cassandra.py		 # ETL builder
|
|____images                      # Referenced image for new dataset
| |____image_event_datafile_new
```

### Example of query and results for song play analysis
##### 1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
```
SELECT 
        artist_name,
        song_title, 
        song_lengh 
FROM artist_songs 
WHERE session_id = 338 AND item_in_session = 4
```

### Result
```
  | artist_name	      | song_title                           | song_lengh
--------------------------------------------------------------------------
0 |	Faithless     | Music Matters (Mark Knight Dub)      | 495.307312
```

##### 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
```
SELECT 
        artist_name, 
        song_title, 
        first_name, 
        last_name 
FROM user_songs 
WHERE user_id = 10 AND session_id = 182
```

### Result
```
  | artist_name       | song_title                | first_name | last_name
--------------------------------------------------------------------------------
0 | Down To The Bone  | Keep On Keepin' On        | Sylvie     | Cruz
1 | Three Drives      | Greece 2000               | Sylvie     | Cruz
2 | Sebastien Tellier | Kilometer                 | Sylvie     | Cruz
3 | Lonnie Gordon     | Catch You Baby (Steve ... | Sylvie     | Cruz
```
##### 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
```
SELECT 
        first_name, 
        last_name 
FROM listened_songs 
WHERE song_title = 'All Hands Against His Own
```

### Result
```
  | first_name 	 | last_name
------------------------------
0 | Jacqueline 	 | Lynch
1 | Tegan 	 | Levine
2 | Sara 	 | Johnson
```