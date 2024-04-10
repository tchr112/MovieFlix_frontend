
from connect import * 

def update_record():
    dbCon, dbCursor = db_access()
    try:
        # check if FilmID exists before updating
        film_id=int(input("Enter the filmID to update a record: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))

        row = dbCursor.fetchone()
        if row == None:
            print(f"No record with the filmID {film_id} exists")

        else:
            num_fields = input("Enter N to upate one field or Y to update all fields").upper()

            if num_fields=="Y":
                title = input("Enter value to update film Title")
                yearReleased = int(input("Enter value to update release year"))
                rating = (input("Enter value to update rating"))
                duration = int(input("Enter value to update film length (minutes)"))
                genre = input("Enter value to updates film genre")

                # perform the update
                dbCursor.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ? ", (title,yearReleased,rating,duration,genre,))
                dbCon.commit()
                print(f"Record {film_id} updated")

            elif num_fields=="N":
                field_name = input("Enter the field (title, yearReleased, rating, duration, genre))")
                field_value = input(f"Enter the value for the field {field_name}: ")

                # perform the update
                dbCursor.execute(f"UPDATE tblfilms SET {field_name} = ? WHERE FilmID = ? ", (field_value,film_id,))
                dbCon.commit()
                print(f"Record {film_id} updated")
            else:
                print(f"Invalid entry")

    except sql.ProgrammingError as e:
        print(f"Programming Error: {e}")

if __name__=="__main__":
    update_record()