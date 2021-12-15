# Import Python packages
import pandas as pd
import os
import glob
import csv
from sql_queries import *
from create_tables import *


def process_data(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.csv'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))


    full_data_rows_list = []

    # for every filepath in the file path list
    for f in all_files:

    # reading csv file
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)

     # extracting each data row one by one and append it
            for line in csvreader:
                #print(line)
                full_data_rows_list.append(line)
        print('{}/{} files processed.'.format(f, num_files))

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('../data/event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

    # check the number of rows in your csv file
    with open('../data/event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print('\n' + '{} rows processed.'.format(sum(1 for line in f)))

def sample_queries(session, query):
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    df = pd.DataFrame(rows._current_rows)
    print(df)

def main():
    """
    Description: This function is responsible for run the ETL pipeline process.
    - Establishes connection with the sparkify database and gets cursor to it.
    - Read the event files in its directory, and then execute the ingest process
    for each file and save it to the database
    - Finally, closes the connection.

    Arguments:
        None

    Returns:
        None
    """

    # This should delete all previous table if exists and create the new ones
    prepare_db()

    # This should preprocess all csv files
    process_data(filepath='../data/event_data')

    # This should insert data in the tables
    insert_data(filepath='../data/event_datafile_new.csv')

    # This should make a connection to a Cassandra instance your local machine
    session, cluster = connect_database()

    for query in queries:
        print ('\n' + queries_title[queries.index(query)])
        sample_queries(session,query)

    # Close conection and cluster
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()