from .application_controller import ApplicationController
from bottle import request, HTTPResponse
from db_engine import sql_engine
from models.artist import Artist
from decorators import auth_route


class ArtistController(ApplicationController):

    @auth_route
    def create(self):
        data = request.json
        session = sql_engine()
        message = "Artist Creation Failed"
        success = False
        issue = None
        try:
            stmt = Artist(
                name=data['name'],
                dob=data['dob'],
                address=data['address'],
                gender=data['gender'],
                first_release_year=data['first_release_year'],
                no_of_albums_released=data['no_of_albums_released']
            )
            session.add(stmt)
            session.commit()
            message = "Artist Created Successfully"
            success = True
        except Exception as e:
            session.rollback()
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
        success = False
        message = "Artist Updated Failed"
        issue = None
        session = sql_engine()
        try:
            artist = session.query(Artist).filter_by(id=data['artist_id'])
            if artist:
                artist.update({
                    'name': data['name'],
                    'dob': data['dob'],
                    'address': data['address'],
                    'gender': data['gender'],
                    'first_release_year': data['first_release_year'],
                    'no_of_albums_released': data['no_of_albums_released']
                })
                session.commit()
                success = True
                message = "Artist Updated Successfully"

        except Exception as e:
            session.rollback()
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
    def delete(self, artist_id):
        session = sql_engine()
        success = False
        message = "Artist Deletion Failed"
        issue = None
        try:
            artist = session.query(Artist).filter_by(id=artist_id).first()
            if artist:
                session.delete(artist)
                session.commit()
                success = True
                message = "Artist Deleted Successfully"
            else:
                issue = "Artist not found"

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