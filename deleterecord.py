
from connect import * 

def delete_record():
    try:
        dbCon, dbCursor = db_access()

        film_id=int(input("Enter the filmID to delete a record"))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))

        row = dbCursor.fetchone()
        if row == None:
            print(f"No record with filmID {film_id} in the films table!")
        else: 
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?",(film_id,)) 
            dbCon.commit()
            print(f"Record {film_id} deleted from the films table")
    except sql.ProgrammingError as e:
        print(f"Delete operation failed: {e}")
if __name__=="__main__":
    delete_record() 