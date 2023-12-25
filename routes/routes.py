from bottle import Bottle, request, template, redirect, get, post
from db.db_connector import *
from validations.user_validation import SignUpUserForm


@get('/')
def welcome():
    return "Welcome page"


@get('/login')
def login_page():
    return template('login')


@post('/login', name='login')
def login():
    data = dict(request.params)


@get('/signup', name='signup_page')
def signup_page():
    return template('signup')


@post('/signup', name='signup')
def signup():
    params = SignUpUserForm(request.params)
    if not params.validate():
        errors = params.errors
        print(errors)
        redirect('signup')

    data = dict(request.params)
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        if connection.is_connected():
            insert_query = """
                INSERT INTO users (first_name, last_name, email, password, phone, gender, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                data['first_name'],
                data['last_name'],
                data['email'],
                data['password'],
                data['phone'],
                data['gender'],
                data['address']
            ))
            connection.commit()

        else:
            error = "Database connection failed"
            redirect('signup')
    except Exception as e:
        connection.rollback()
        error = "Something went wrong"
        redirect('signup')
    finally:
        cursor.close()
        connection.close()
        redirect('login')











