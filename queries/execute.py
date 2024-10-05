# imports
import sqlite3
import queries as q


def execute_query(db_name, query):
    """
    Executes a given SQL query on the specified SQLite database
    and converts it into a pandas DataFrame object.

    Parameters:
        db_name (str): The name of the SQLite database file.
        query (str): The SQL query to execute.

    Returns:
        result (DataFrame): The result of the query (if any).
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)

        # Create the cursor object
        cursor = conn.cursor()

        # execute the query
        cursor.execute(query)

        # save the results of the query to a variable
        results = cursor.fetchall()

        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


if __name__ == "__main__":
    # save the path to the sqlite3 database
    DB_PATH = '../databases/rpg/rpg_db.sqlite3'

    # use the execute_query function
    rows = execute_query(DB_PATH, q.SELECT_ALL)

    # print the rows
    for row in rows:
        print(row)
