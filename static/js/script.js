
// expanding Add Records Menu
document.getElementById('add_records_btn').addEventListener('click', function() {
    console.log('click')
    
    // ensure correct table is displaying:
    var all_table = document.getElementById('all_table');
    var display_table = document.getElementById('display_table');
    all_table.classList.add('show')
    display_table.classList.remove('show')
    
    // Toggle the visibility of the hidden content
    var add_records = document.getElementById('add_records');
    var display_records = document.getElementById('display_records')
    if (add_records.classList.contains('show')) {
        add_records.classList.remove('show');
    } else {
        add_records.classList.add('show')
        delete_records.classList.remove('show');
        amend_records.classList.remove('show')
        display_records.classList.remove('show')
    }
    });

//  Disabling input field submit method
document.getElementById("add_data_form").addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission behavior
});

// enabling custom submit button on Add records
document.getElementById('submit_button').addEventListener('click', function() {
    submitFormData();
});

// submit input data for add_record:
function submitFormData() {
    // Fetch data from input fields
    var title = document.getElementById('title').value;
    var release_year = document.getElementById('release_year').value;
    var rating = document.getElementById('rating').value;
    var runtime = document.getElementById('runtime').value;
    var genre = document.getElementById('genre').value;
    var formData = new FormData();

    formData.append('title', title);
    formData.append('release_year', release_year);
    formData.append('rating', rating);
    formData.append('runtime', runtime);
    formData.append('genre', genre);
    add_rtn_val = false
    formData.forEach(value=>{
        console.log(value)

        if (value===''){
            console.log("error missing value")
            if (add_rtn_val){
            return
            }
            else{
            add_error_message()
            }   
            add_rtn_val = true
        }
    })
    if (add_rtn_val){
        return
    }
    else {
        fetch('/add_film', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            // Handle response from server if needed
            console.log(data); // Log response to console
            console.log('reloading...')
            location.reload();
        })
        .catch(error => {
            console.error('Error:', error); // Log any errors to console
        });
    }
}

// add error message:
function add_error_message(){
    if (add_rtn_val = true){
    error_message = document.getElementById('add_error_message')
    error_message.classList.add('show')
}
}



// expanding Delete Records Menu
document.getElementById('delete_records_btn').addEventListener('click', function() {
    console.log('click')
    // ensure correct table is displaying:
    var all_table = document.getElementById('all_table');
    var display_table = document.getElementById('display_table');
    all_table.classList.add('show')
    display_table.classList.remove('show')
    
    // Toggle the visibility of the hidden content
    var delete_records = document.getElementById('delete_records');
    var display_records = document.getElementById('display_records')
    if (delete_records.classList.contains('show')) {
        delete_records.classList.remove('show');
    } else {
        add_records.classList.remove('show')
        delete_records.classList.add('show');
        amend_records.classList.remove('show')
        display_records.classList.remove('show')
    }
    });
    


//  Disabling input field submit method for delete records
document.getElementById("delete_data_form").addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission behavior
});


    // enabling custom submit button on delete records
document.getElementById('delete_button').addEventListener('click', function() {
    delete_record();
});

// delete function:
function delete_record(){
    del_filmID = document.getElementById('del_filmID').value
    var formData = new FormData()
    formData.append('filmID', del_filmID)
    fetch('/del_film',{
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data =>{
        console.log('test')
        console.log(data)
        if (data.includes('deleted')){
            console.log('reloading...')
            location.reload();
        }
        else {
            // error message
            console.log('changing')
            del_error_message(del_filmID)
        }
    })
    .catch(error => {
        console.error('Error',error)
    })
}

// delete error message:
function del_error_message(name){
    del_error_filmID = document.getElementById('del_error_filmID')
    del_error_filmID.textContent = name
    error_message = document.getElementById('del_error_message')
    error_message.classList.add('show')

}



// expanding Amend Records Menu

document.getElementById('amend_records_btn').addEventListener('click', function() {
    console.log('click')
    // ensure correct table is displaying:
    var all_table = document.getElementById('all_table');
    var display_table = document.getElementById('display_table');
    all_table.classList.add('show')
    display_table.classList.remove('show')
    // Toggle the visibility of the hidden content
    var amend_records = document.getElementById('amend_records');
    var display_records = document.getElementById('display_records')
    if (amend_records.classList.contains('show')) {
        amend_records.classList.remove('show');
    } else {
        add_records.classList.remove('show')
        delete_records.classList.remove('show');
        amend_records.classList.add('show')
        display_records.classList.remove('show')
    }
    });


//  Disabling input field submit method for amend records
document.getElementById("amend_data_form").addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission behavior
});


    // enabling custom submit button on amend records button 1
document.getElementById('amend_button_1').addEventListener('click', function() {
    amend_record_option_selection();
});

    // enabling custom submit button on amend records button 2 
    document.getElementById('amend_button_2').addEventListener('click', function() {
        amend_record();
    });



// Adapting menu to change options for amending one record vs all records:
function amend_record_option_selection(){
    amend_filmID = document.getElementById('amend_filmID').value
    amend_update = document.getElementById('amend_update').value
    console.log(amend_update)
    var formData = new FormData()
    formData.append('filmID', amend_filmID)
    fetch('/check_filmID',{
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data =>{
        console.log('test')
        console.log(data)
        if (data.includes('No record')){
            console.log('Error: No record with this filmID')
            amend_error_message(amend_filmID)
        }
        else {
            if (amend_update=='one_record'){
                one_expand_amend_options()
            }
            else if (amend_update=='all_records'){
                all_expand_amend_options()
            }
        }
    })
    .catch(error => {
        console.error('Error',error)
    })
}

// amend menu functionality
function amend_record(){


    amend_filmID = document.getElementById('amend_filmID').value
    amend_update = document.getElementById('amend_update').value
    console.log(amend_update)
    var formData = new FormData()
    formData.append('filmID', amend_filmID)
    formData.append('amend_update', amend_update)
    if (amend_update=='one_record'){
        var one_category = document.getElementById('amend_update').value
        var one_amend_category = document.getElementById('one_amend_category').value
        var one_amend_content = document.getElementById('one_amend_content').value
        formData.append('amend_update',one_category)
        formData.append('one_amend_category', one_amend_category)
        formData.append('one_amend_content', one_amend_content)
        console.log('one changed')
    }

    if (amend_update == 'all_records'){
        var all_categories = document.getElementById('amend_update').value
        var all_title = document.getElementById('all_title').value;
        var all_release_year = document.getElementById('all_release_year').value;
        var all_rating = document.getElementById('all_rating').value;
        var all_runtime = document.getElementById('all_runtime').value; 
        var all_genre = document.getElementById('all_genre').value;
        formData.append('amend_update',all_categories)
        formData.append('all_title',all_title)
        formData.append('all_release_year',all_release_year)
        formData.append('all_rating',all_rating)
        formData.append('all_runtime',all_runtime)
        formData.append('all_genre',all_genre)
        console.log('all changed')
        console.log(formData)
    }
    fetch('/amend_film',{
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data =>{
        console.log('test')
        console.log(data)
        if (data.includes('updated')){
            console.log('reloading...')
            location.reload();
        }
        else if (data.includes('no record')) {
            // error message
            console.log('displaying error...')
            amend_error_message(amend_filmID)
        }
    })
    .catch(error => {
        console.error('Error',error)
    })
}




// amend error message:
function amend_error_message(name){
    amend_error_filmID = document.getElementById('amend_error_filmID')
    amend_error_filmID.textContent = name
    error_message = document.getElementById('amend_error_message')
    error_message.classList.add('show')
}

// one amend options:
function one_expand_amend_options(){
    one_amend_expand = document.getElementById('one_amend_expand')
    amend_records_menu = document.getElementById('amend_records_menu')
    var amend_button_1 = document.getElementById('amend_button_1')
    var amend_button_2 = document.getElementById('amend_button_2')
    error_message = document.getElementById('amend_error_message')
    one_amend_expand.classList.add('show')
    amend_records_menu.classList.remove('show')
    amend_button_1.classList.remove('show')
    amend_button_2.classList.add('show')
    error_message.classList.remove('show')
    console.log('one changed')
}

// all amend options:
function all_expand_amend_options(){
    all_amend_expand = document.getElementById('all_amend_expand')
    amend_records_menu = document.getElementById('amend_records_menu')
    var amend_button_1 = document.getElementById('amend_button_1')
    var amend_button_2 = document.getElementById('amend_button_2')
    error_message = document.getElementById('amend_error_message')
    all_amend_expand.classList.add('show')
    amend_records_menu.classList.remove('show')
    amend_button_1.classList.remove('show')
    amend_button_2.classList.add('show')
    error_message.classList.remove('show')
    console.log('all changed')
}



// expanding Display Records Menu

document.getElementById('display_records_btn').addEventListener('click', function() {
    console.log('click')
    // Toggle the visibility of the hidden content
    var display_records = document.getElementById('display_records');
    if (display_records.classList.contains('show')) {
        display_records.classList.remove('show');
    } else {
        add_records.classList.remove('show')
        delete_records.classList.remove('show');
        amend_records.classList.remove('show')
        display_records.classList.add('show')
    }
    });


//  Disabling input field submit method for display records
document.getElementById("display_criteria").addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission behavior
});


    // enabling custom submit button on display records button 1
document.getElementById('display_records_submit').addEventListener('click', function() {
    display_records();
});

function display_records(){
    // switching tables
    var all_table = document.getElementById('all_table');
    var display_table = document.getElementById('display_table');
    all_table.classList.remove('show')
    display_table.classList.add('show')

    var display_category = document.getElementById('display_category').value
    var display_criteria = document.getElementById('display_criteria').value
    console.log(`1: ${display_category}, 2: ${display_criteria}`)
    var formData = new FormData()
    formData.append('display_category', display_category)
    formData.append('display_criteria', display_criteria)
    fetch('/display_records',{
        method: 'POST',
        body: formData
    })
    .then(response=>response.json())
    .then(data=>{
        console.log('test')
        console.log(data)
        update_display_table(data)
    })
    .catch(error=> {
        console.error('error', error)
    })
}

function update_display_table(data){
    var display_table_body=document.getElementById('display_table_body')
    console.log(data)
    display_table_body.innerHTML=''
    data.forEach(film=>{
        var row = document.createElement('tr')
        film.forEach(cell=>{
            var cell_element = document.createElement('td')
            cell_element.textContent=cell 
            row.appendChild(cell_element)
        })
        display_table_body.appendChild(row)
    })
}