import os
from flask import Flask

""" Instance from app
:param app: instance from application flask
:type app: Flask
"""
__config = {}


def initialize_config(app):
    """Load config in 'app.config'
    :param app: instance from application flask
    :type app: Flask
    """
    __config['YOUTUBE_KEY'] = os.getenv('YOUTUBE_KEY')
    __config['CALLBACK'] = os.getenv('CALLBACK')

def get_youtube_key():
    return __config['YOUTUBE_KEY']
