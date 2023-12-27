import bottle
# from sqlalchemy import URL, create_engine
# from db_engine import sql_engine
from routes import setup_routes


class MainApp:

    def __init__(self, host, port, db_host, db_port):
        self.host = host
        self.port = port
        self.db_host = db_host
        self.db_port = db_port

        self.app = bottle.default_app()

        # initialize the routes

        setup_routes(self.app)

        # db engine and db setup

        # run the test
        self.app.run(host=self.host, port=self.port, debug=True, reloader=True)
