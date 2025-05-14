# imports
import sqlite3
import northwind_queries as nw
import rpg_queries as rpg


def execute_query(db_name, query):
    """
    Executes a given SQL query on the specified SQLite database.

    Parameters:
        db_name (str): The name of the SQLite database file.
        query (str): The SQL query to execute.

    Returns:
        result: The result of the query (if any)
    """
    # Ensure the conn variable defined
    conn = None

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
    RPG_DB = '../databases/rpg/rpg_db.sqlite3'
    NORTHWIND_DB = "../databases/northwind/northwind.db"

    # use the execute_query function
    rows = execute_query(NORTHWIND_DB, nw.NUM_SUPPLIERS_BY_REGION)

    # check if rows is None before iterating
    if rows is not None:
        # print the rows
        for row in rows:
            print(row)
    else:
        print("Data not returned or an error occurred while executing the query.")
