import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.controllers import Clima
from api.database import init_db

app = Flask(__name__)
load_dotenv()
environment_configuration = os.getenv('CONFIGURATION_SETUP',"None")
app.config.from_object(environment_configuration)
init_db(app)
CORS(app)

api = Api(app)


api.add_resource(Clima, '/clima','/clima')

if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0', port=5000)