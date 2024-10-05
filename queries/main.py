# imports
import sqlite3
import pandas as pd
import queries as q


def execute_query(db_name, query) -> pd.DataFrame:
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

        # create a pandas dataframe with the query
        df = pd.read_sql_query(query, conn)

        return df

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


if __name__ == "__main___":
    db_name = 'rpg_db.sqlite3'

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM charactercreator_character")
    results = cursor.fetchall()

    print(results)

    cursor.close()
