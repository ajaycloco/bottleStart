import bottle
from routes import setup_routes
from bottle import response, app
from bottle_cors_plugin import CorsPluginObject
from bottle_cors_plugin import cors_plugin


class MainApp:

    def __init__(self, host, port, db_host, db_port):
        self.host = host
        self.port = port
        self.db_host = db_host
        self.db_port = db_port

        self.app = app()

        setup_routes(self.app)

        # run the test
        self.app.install(cors_plugin('*'))

        self.app.run(host=self.host, port=self.port, debug=True, reloader=True)
