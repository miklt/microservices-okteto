import os
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
environment_configuration = os.environ.get('CONFIGURATION_SETUP')
app.config.from_object(environment_configuration)
CORS(app)
api = Api(app)


class Clima(Resource):
    def get(self):
        return {'hour': '17h00','city':'São Paulo','temperature':'29.0'}

api.add_resource(Clima, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)