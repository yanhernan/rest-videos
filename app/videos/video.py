from flask import request, abort
from flask_restful import Resource
from utils import response_json
from youtube import search_videos

class VideosApi(Resource):

    def get(self, *args, **kwargs):
        search = ''
        if 'search' in request.args:
            search = request.args['search']
        videos = search_videos(search)
        return response_json(videos, 200)
