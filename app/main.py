import os
from flask import Flask, Blueprint
from flask_restful import Api
from videos import initialize_routes_videos
from config import initialize_config

app = Flask(__name__, instance_relative_config=True)
# load config values
initialize_config(app)
# create route prefix
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
# Load route prefix
api = Api(blueprint)
# Register route prefix
app.register_blueprint(blueprint)
# init routes
initialize_routes_videos(api)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)