from flask_restful import Api

from api.resources.champions import Champion

api = Api()

api.add_resource(Champion, '/api/champion')