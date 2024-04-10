
import sqlite3 as sql


def db_access():
    try:
        with sql.connect("filmflix.db") as dbCon: 

            dbCursor = dbCon.cursor()

            return dbCon, dbCursor
        
    except sql.OperationalError as e: 

        print(f"Connection failed: {e}")


if __name__ == "__main__":
    db_access()

