"Objectives"
"" '' # Import connect module

from connect import *

"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

# Create a function to read record(s) from a table in a database
def read_records():
    # try:
        dbCursor = db_access()[1]
        # invoke the cursor, execute method to select all the records from the table
        dbCursor.execute("SELECT * FROM tblFilms")

        #  fetch all selected records using the fetchall method and assigned it to a variable
        
        all_records = dbCursor.fetchall() # fetchall method fetches the selected records

        dbCursor.close()
        return(all_records)
        # if all_records:
        #     # display a line of 100 asteriks from left to right 
        #     print("*" * 100)
        #     # format the heading using field names: SongID, Title, Artist, Genre 
        #     print(f"filmID{' ':<3}|Title{' ':<30}|YearReleased{' ':<2}|Rating{' ':<4}|Duration{' ':<2}|Genre{' ':<15}")
        #     print("*" * 100)

        #     for records in all_records:
        #         # 0         1       3       4
        #         # SongID    Title   Arist   Genre
        #         # 1         Test    Tester  Coding
        #         print(f"{records[0]:<9}|{records[1]:<35}|{records[2]:<14}|{records[3]:<10}|{records[4]:<10}|{records[5]:<20}")
        #         print("-"*100)

    # except sql.OperationalError as e:
    #     print(f"Failed because: {e}")
# films = read_records()
# print(films)

if __name__=="__main__":
    read_records()


                #     print("*" * 100)
                # print(f"filmID{' ':<3}|Title{' ':<30}|YearReleased{' ':<2}|Rating{' ':<4}|Duration{' ':<2}|Genre{' ':<15}")
                # for records in rows:
                #     print("*" * 100)
                #     print(f"{records[0]:<9}|{records[1]:<35}|{records[2]:<14}|{records[3]:<10}|{records[4]:<10}|{records[5]:<20}")
                # print("-"*100)