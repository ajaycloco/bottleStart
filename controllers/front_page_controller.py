from controllers.application_controller import ApplicationController
from bottle import template


class FrontPageController(ApplicationController):
    def landing_page(self):
        return template('index.tpl')
