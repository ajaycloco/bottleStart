import bottle
from routes import setup_routes
from beaker.middleware import SessionMiddleware
class MainApp:

    def __init__(self, host, port, db_host, db_port):
        self.host = host
        self.port = port
        self.db_host = db_host
        self.db_port = db_port

        self.app = bottle.default_app()

        # initialize the routes
        setup_routes(self.app)

        # set up session
        session_options = {
            'session.type': 'memory',  # Use in-memory storage
            'session.auto': True,
        }
        SessionMiddleware(self.app, session_options)

        # run the test
        self.app.run(host=self.host, port=self.port, debug=True, reloader=True)
