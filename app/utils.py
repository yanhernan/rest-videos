from flask import Response
from json import dumps

def response_json(data, status):
    return Response(dumps(data), mimetype="application/json", status=status)
