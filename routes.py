from controllers.auth_controller import AuthController
from controllers.front_page_controller import FrontPageController
from controllers.user_controller import UserController

def setup_routes(app):
    app.route('/', 'GET', FrontPageController().landing_page)
    app.route('/login', 'GET', FrontPageController().login_page)

    app.route('/users/create', 'POST', UserController().signup)
    app.route('/login', 'POST', AuthController().login)
