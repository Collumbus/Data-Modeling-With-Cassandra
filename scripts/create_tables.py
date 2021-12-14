import cassandra
import os
import csv
from sql_queries import create_table_queries, drop_table_queries, artist_songs_table_insert, user_songs_table_insert, listened_songs_table_insert


def connect_database():
    """
    Description:
    - Connects to the sparkifydb
    - Returns the cluster and session to sparkifydb

    Arguments:
        None.

    Returns:
        cluster, session.
    """

    # This should make a connection to a Cassandra instance your local machine
    from cassandra.cluster import Cluster
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
    except Exception as e:
        print(e)

    # To establish connection and begin executing queries, need a session
    try:
        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS sparkify 
            WITH REPLICATION = 
            { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
            """
        )
    except Exception as e:
        print(e)

    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)

    return session, cluster


def drop_tables(session):
    """
    Description: Drops each table using the queries in `drop_table_queries` list.

    Arguments:
        session: the cursor object.

    Returns:
        None.
    """
    for query in drop_table_queries:
        session.execute(query)


def create_tables(session):
    """
    Description: Creates each table using the queries in `create_table_queries` list.

    Arguments:
        session: the cursor object.

    Returns:
        None.
    """
    for query in create_table_queries:
        session.execute(query)

def insert_data(filepath):
    """
    Description:
    -

    Arguments:
        None.

    Returns:
        None.
    """

    # This should make a connection to a Cassandra instance your local machine
    session, cluster = connect_database()

    with open(filepath, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(artist_songs_table_insert, (line[0], line[9], float(line[5]), int(line[8]), int(line[3])))
            session.execute(user_songs_table_insert, (line[0], line[9], line[1], line[4], int(line[10]), int(line[8]), int(line[3])))
            session.execute(listened_songs_table_insert, (int(line[10]), line[1], line[4], line[9]))
        print('All data has been inserted in the tables.')

    session.shutdown()
    cluster.shutdown()

def prepare_db():
    """
    Description:
    - Drops (if exists) and Creates the sparkify database.

    - Establishes connection with the sparkify database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.

    Arguments:
        None.

    Returns:
        None.
    """
    # This should make a connection to a Cassandra instance your local machine
    session, cluster = connect_database()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()