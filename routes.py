from controllers.front_page_controller import FrontPageController


def setup_routes(app):
    app.route('/', 'GET', FrontPageController().landing_page)








