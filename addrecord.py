from connect import *


def insert_record():

    try:
        dbCon, dbCursor = db_access()

        title = input("Please input film Title").title()
        yearReleased = int(input("Please input release year of selected film"))
        rating = (input("What rating was the film?")).upper()
        duration = int(input("How long is the film in minutes?"))
        genre = input("What genre is the film?").title()


        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)",(title,yearReleased,rating,duration,genre,))

        dbCon.commit() 
        print(f"{title} inserted in the Films table")
    except sql.OperationalError as e:
        print(f"Failed: {e}")

    except sql.ProgrammingError() as pe:
        print(f"Not working because:{pe}")

    except sql.Error as er:
        print(f"Failed due to: {er}")

if __name__ == "__main__":
    insert_record()