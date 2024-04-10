
from connect import *

def printall(option):

        dbCon, dbCursor = db_access()
        if option == 1:
            dbCursor.execute("SELECT * FROM tblFilms")
            rows = dbCursor.fetchall()
            if option == 1:
                print("*" * 100)
                print(f"filmID{' ':<3}|Title{' ':<30}|YearReleased{' ':<2}|Rating{' ':<4}|Duration{' ':<2}|Genre{' ':<15}")
                for records in rows:
                    print("*" * 100)
                    print(f"{records[0]:<9}|{records[1]:<35}|{records[2]:<14}|{records[3]:<10}|{records[4]:<10}|{records[5]:<20}")
                print("-"*100)
            else: 
                print("n/a")

        elif option in [2,3,4]:
            if option == 2:
                category = "Genre"
            if option == 3:
                category = "yearReleased"
            if option == 4:
                category = "rating"
            search_field = str(input(f"Please specificy {category} :")).title()
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {category} LIKE ?", (f"%{search_field}%",))
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with {category}: {search_field}, please re-enter {category}")

            else:
                print("hello")
                print("*" * 100)
                print(f"filmID{' ':<3}|Title{' ':<30}|YearReleased{' ':<2}|Rating{' ':<4}|Duration{' ':<2}|Genre{' ':<15}")
                for records in rows:
                    print("*" * 100)
                    print(f"{records[0]:<9}|{records[1]:<35}|{records[2]:<14}|{records[3]:<10}|{records[4]:<10}|{records[5]:<20}")
                print("-"*100)
            

        else:
            print("error")
    