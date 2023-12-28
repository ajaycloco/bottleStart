from bottle import request, HTTPResponse
from token_config import validate_token


def auth_route(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        res_body = {
            "success": False,
            "message": "Invalid Token or Token expired",
            "status": 403
        }
        if token:
            is_token_valid = validate_token(token.split("Bearer ")[-1])
            if not is_token_valid:
                return HTTPResponse(body=res_body)
            else:
                return func(*args, **kwargs)
        else:
            return HTTPResponse(body=res_body)

    return wrapper
