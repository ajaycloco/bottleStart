import datetime
import environs
import jwt
from db_engine import sql_engine
from models.user import User

env = environs.Env()
env.read_env()
secret_key = env.str('jwt_secret')
algorithm = "HS256"


def generate_token(payload):
    token = jwt.encode(payload, secret_key, algorithm)

    return token


def validate_token(token):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithm)
        session = sql_engine()

        if 'exp' in decoded_payload and 'user_id' in decoded_payload and 'email' in decoded_payload:
            user = session.query(User).filter_by(email=decoded_payload['email'], id=decoded_payload['user_id']).first()
            if datetime.datetime.utcfromtimestamp(
                    decoded_payload['exp']) > datetime.datetime.utcnow() and user is not None:
                return True
            else:
                return False
        return False
    except Exception as e:
        return False


def generate_refresh_token(access_token):
    decoded_payload = jwt.decode(access_token, secret_key, algorithm)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)

    refresh_payload = {
        'user_id': decoded_payload['id'],
        'email': decoded_payload['email'],
        'exp': expiration_time
    }

    # Generating the refresh token
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm)

    return refresh_token
