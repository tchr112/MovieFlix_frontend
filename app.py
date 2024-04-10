
# NOTES TO SELF:

# need to extend this to work with delete record as well.
# need to link delete_record sql code to delete record button.




from flask import Flask, render_template, url_for, request, redirect, jsonify
# from flask import Flask, render_template
import addrecord, amendrecord, deleterecord, read_records
import sqlite3 as sql
from printall import printall


app = Flask(__name__)   
# app.run(debug=True)

def db_access():
    with sql.connect("filmflix.db") as dbCon: 
        dbCon.row_factory = sql.Row

        return dbCon

# display files
@app.route('/')
def index(): 
    conn = db_access() 
    films = conn.execute('SELECT * from tblFilms').fetchall() 
    conn.close()
    return render_template('index.html', title='Home', films=films)


# add records
@app.route('/add_film', methods=['POST'])
def add_film():
    try:
        title = request.form['title']
        release_year = request.form['release_year']
        rating = request.form['rating']
        duration = request.form['runtime']
        genre = request.form['genre']
        conn = db_access()
        films = conn.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)",(title,release_year,rating,duration,genre,))
        conn.commit()
        conn.close()
        return (f"{title} inserted in the Films table")

    except Exception as e:
        return(f'an error has occured: {e}')

@app.route('/del_film', methods=['POST'])
def del_film():
    filmID = request.form['filmID']
    print(filmID)
    conn = db_access()
    films = conn.execute("SELECT * FROM tblFilms WHERE filmID = ?",(filmID,)).fetchone()
    if films == None:
        return f"No record with filmID {filmID} in the films table"
    else:
        conn.execute("DELETE FROM tblFilms WHERE filmID = ?",(filmID,))
        conn.commit()
        conn.close()
        return f'Film with filmID {filmID} was deleted from the table'
    

# checking if filmID exists for Amend Film section
@app.route('/check_filmID', methods=['POST'])
def check_filmID():
    filmID = request.form['filmID']
    conn = db_access()
    films = conn.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,)).fetchone()
    conn.close()
    if films == None:
        return f'No record with filmID {filmID} in the films table'
    else:
        return f'filmID present'


@app.route('/amend_film', methods=['POST'])
def amend_film():
    filmID = request.form['filmID']
    amend_update = request.form['amend_update']

    if amend_update == 'one_record':
    # update one record:
        one_amend_content=request.form['one_amend_content']
        one_amend_category=request.form['one_amend_category']

    elif amend_update == 'all_records':
    # update all records:
        title=request.form['all_title']
        year_released=request.form['all_release_year']
        rating=request.form['all_rating']
        duration=request.form['all_runtime']
        genre=request.form['all_genre']

    conn = db_access()
    films = conn.execute("SELECT * FROM tblFilms WHERE filmID = ?",(filmID,)).fetchone()
    if films == None:
        return f"No record with filmID {filmID} in the films table"
    else:
        if amend_update == 'one_record':
            conn.execute(f"UPDATE tblfilms SET {one_amend_category} = ? WHERE FilmID = ? ", (one_amend_content,filmID,))
            conn.commit()
            conn.close()
            return f'Film with filmID {filmID} was updated from the table'
        elif amend_update == 'all_records':
            conn.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ? ", (title,year_released,rating,duration,genre,filmID,))
            conn.commit()
            conn.close()
            return f'Film with filmID {filmID} was updated from the table'



# display_records
@app.route('/display_records', methods = ['POST'])
def display_records(): 
    conn = db_access() 
    display_category = request.form['display_category']
    display_criteria =  request.form['display_criteria']
    display_films = conn.execute(f'SELECT * from tblFilms where {display_category} LIKE ?',(f'%{display_criteria}%',)).fetchall() 
    conn.close()
    display_films_list = [list(film) for film in display_films]
    return jsonify(display_films_list)


# f'Record {filmID} deleted from the films table'

    # film_id=int(input("Enter the filmID to delete a record"))
    # dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id,))

    # row = dbCursor.fetchone()
    # if row == None:
    #     print(f"No record with filmID {film_id} in the films table!")
    # else: 
    #     dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?",(film_id,)) 
    #     dbCon.commit()
    #     print(f"Record {film_id} deleted from the films table")



# return(f"received film ID: {filmID}")

if __name__ == '__main__':
    app.run(debug=True)

# index()

# function to read from a text file
"""
def read_file(file_path): 
    try:
        with open(file_path) as open_file:
            rf = open_file.read()

            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")


# Main Menu
def films_menu():
    try:
        option = 0 
        optionList = ["1","2","3","4","5"]
        menu_choice = read_file("dbMenu.txt")


        while option not in optionList:
            print(menu_choice)
            option = input("Select an option from the menu above: ")
            if option not in optionList:
                print(f"{option} not a valid choice")
            
        return option
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Sub Menu
def reports_sub_menu():
    try:
        sub_menu_option = 0 
        sub_menu_optionList = ["1","2","3","4","5"] 
        submenu_choice = read_file("reportMenu.txt")
        
        while sub_menu_option not in sub_menu_optionList:
            print(submenu_choice)
            sub_menu_option = input("Select an option from the menu above: ")
            if sub_menu_option not in sub_menu_optionList:
                print(f"{sub_menu_option} not a valid choice")
            
        return sub_menu_option
    except FileNotFoundError as e:
        print(f"Error: {e}")

mainProgram = True 
subProgram = False
looper = True

while looper:

    while mainProgram: 
        main_menu = films_menu()

        if main_menu == "1":
            addrecord.insert_record()
        elif main_menu == "2":
            deleterecord.delete_record()
        elif main_menu == "3":
            amendrecord.update_record()
        elif main_menu == "4":
            read_records.read_records()
        else: 
            mainProgram = False
            looper = False 

    if subProgram:
        while subProgram: 
            sub_main_menu = reports_sub_menu()

            if sub_main_menu == "1":
                printall(1)
            elif sub_main_menu == "2":
                printall(2)
            elif sub_main_menu == "3":
                printall(3)
            elif sub_main_menu == "4":
                printall(4)
            elif sub_main_menu == "5":
                print("returning")
                mainProgram = True
                subProgram = False
                break

                """