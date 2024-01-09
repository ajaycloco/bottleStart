from controllers.auth_controller import AuthController
from controllers.front_page_controller import FrontPageController
from controllers.music_controller import MusicController
from controllers.user_controller import UserController
from controllers.artist_controller import ArtistController
from bottle import response


def setup_routes(app):
    app.route('/', 'GET', FrontPageController().landing_page)
    app.route('/login', 'GET', FrontPageController().login_page)
    app.route('/login', 'POST', AuthController().login)

    app.route('/users/create', 'POST', UserController().signup)

    app.route('/artists', 'GET', ArtistController().get_all)
    app.route('/artists/create', 'POST', ArtistController().create)
    app.route('/artists/update', 'POST', ArtistController().update)
    app.route('/artists/<artist_id>/delete', 'GET', ArtistController().delete)

    app.route('/music/create', 'POST', MusicController().create)
    app.route('/music/update', 'POST', MusicController().update)
    app.route('/music/<music_id>/delete', 'GET', MusicController().delete)
