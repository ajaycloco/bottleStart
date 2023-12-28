from decorators import auth_route
from .application_controller import ApplicationController
from bottle import request, response, HTTPResponse
from db_engine import sql_engine
from models.user import User
from passlib.hash import pbkdf2_sha256


class UserController(ApplicationController):
    @auth_route
    def signup(self):
        data = request.json
        password = pbkdf2_sha256.hash(data['password'])
        session_info = sql_engine()
        success = True
        issue = None
        message = "Successfully Created"
        try:
            stmt = User(
                full_name=data['full_name'],
                email=data['email'],
                password=password,
                status=data['status']
            )
            session_info.add(stmt)
            session_info.commit()
        except Exception as e:
            session_info.rollback()
            success = False
            issue = e.__str__()
            message = "Users Creation Failed"
        finally:
            session_info.close()
            res = {
                'success': success,
                'issue': issue,
                'message': message
            }
            return HTTPResponse(body=res)
