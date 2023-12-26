from app.controllers.application_controller import ApplicationController


class FrontPageController(ApplicationController):

    def landing_page(self):

        return template('header')