from bottle import request, HTTPResponse
from .application_controller import ApplicationController
from db_engine import sql_engine
from models.music import Music
from decorators import auth_route


class MusicController(ApplicationController):

    @auth_route
    def create(self):
        data = request.json
        success = False
        message = "Music Creation Failed"
        issue = None
        session = sql_engine()
        try:
            stmt = Music(
                title=data['title'],
                album_name=data['album_name'],
                genre=data['genre'],
                artist_id=data['artist_id']
            )
            session.add(stmt)
            session.commit()
            success = True
            message = "Music Created Successfully"
        except Exception as e:
            session.rollback()
            success = False
            issue = e.__str__()
        finally:
            session.close()
            res_body = {
                'success': success,
                'message': message,
                'issue': issue
            }
            return HTTPResponse(body=res_body)

    @auth_route
    def update(self):
        data = request.json
        session = sql_engine()
        success = False
        message = "Music Update Failed"
        issue = None
        try:
            music = session.query(Music).filter_by(id=data['music_id'])
            if music.first():
                music.update({
                    'title': data['title'],
                    'album_name': data['album_name'],
                    'genre': data['genre'],
                    'artist_id': data['artist_id']
                })
                session.commit()
                message = "Music Updated Successfully"
                success = True
            else:
                issue = "Music Not found"

        except Exception as e:
            issue = e.__str__()
            session.rollback()

        finally:
            session.close()
            res_body = {
                'success': success,
                'message': message,
                'issue': issue
            }
            return HTTPResponse(body=res_body)

    @auth_route
    def delete(self, music_id):
        success = False
        message = "Music Deletion Failed"
        issue = None
        session = sql_engine()
        try:
            music = session.query(Music).filter_by(id=music_id).first()
            if music:
                session.delete(music)
                session.commit()
                success = True
                message = "Music Deleted Successfully"
            else:
                issue = "Music Not Found"
        except Exception as e:
            issue = e.__str__()
            session.rollback()
        finally:
            session.close()
            res_body = {
                'success': success,
                'message': message,
                'issue': issue
            }
            return HTTPResponse(body=res_body)

