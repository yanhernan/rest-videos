from flask import request, abort
from flask_restful import Resource
from utils import response_json
from youtube import search_videos

class VideosApi(Resource):

    def get(self, *args, **kwargs):
        videos = search_videos(request.args)
        return response_json(videos, 200)
