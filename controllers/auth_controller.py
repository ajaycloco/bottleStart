import datetime

from bottle import request, HTTPResponse
from models.user import User
from .application_controller import ApplicationController
from passlib.hash import pbkdf2_sha256
from token_config import *
from models.token import Token
from db_engine import sql_engine


class AuthController(ApplicationController):
    def login(self):
        db_session = sql_engine()
        response_body = {
            'success': False,
            'status': 400,
            'message': 'Invalid Credentials'
        }
        try:
            data = request.json
            email = data.get('email', None)
            password = data.get('password', None)
            if not email or not password:
                pass

            user = db_session.query(User).filter_by(email=email).first()
            if user and pbkdf2_sha256.verify(password, user.password):
                # generate token
                expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=30)
                token_payload = {
                    'user_id': user.id,
                    'email': user.email,
                    'exp': expiration_date
                }
                token = generate_token(token_payload)

                token_exist = db_session.query(Token).filter_by(user_id=user.id)

                if token_exist.first():
                    token_exist.update({'access_token': token})
                else:
                    stmt = Token(
                        user_id=user.id,
                        access_token=token,
                    )
                    db_session.add(stmt)
                db_session.commit()

                response_body = {
                    'success': True,
                    'status': 200,
                    'message': 'Login Successful',
                    'jwt_access_token': {
                        'access_token': token,
                        'expiration_date': str(expiration_date)
                    }
                }

        except Exception as e:
            response_body = {
                'success': False,
                'status': 400,
                'message': e.__str__()
            }
            db_session.rollback()

        finally:
            db_session.close()
            return HTTPResponse(body=response_body)
