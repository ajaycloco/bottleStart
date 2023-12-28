from .application_controller import ApplicationController
from bottle import template


class FrontPageController(ApplicationController):
    def landing_page(self):
        return template('pages/index.tpl')

    def login_page(self):
        return template('pages/login.tpl')
