from flask_restful import Api
from .video import VideosApi

def initialize_routes(api):
    """ Init routes from videos
    :param api: Api Reference
    :type api: Api
    """
    api.add_resource(VideosApi, '/videos')
