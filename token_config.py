import datetime
import environs
import jwt

env = environs.Env()
env.read_env()
secret_key = env.str('jwt_secret')
algorithm = "HS256"


def generate_token(payload):
    token = jwt.encode(payload, secret_key, algorithm)

    return token


def validate_token(token):
    decoded_payload = jwt.decode(token, secret_key, algorithm)
    if 'exp' in decoded_payload:
        if decoded_payload['exp'] < datetime.datetime.utcnow():
            return False
        else:
            return True
    return False


def generate_refresh_token(access_token):
    decoded_payload = jwt.decode(access_token, secret_key, algorithm)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)

    refresh_payload = {
        'id': decoded_payload['id'],
        'email': decoded_payload['email'],
        'exp': expiration_time
    }

    # Generating the refresh token
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm)

    return refresh_token
