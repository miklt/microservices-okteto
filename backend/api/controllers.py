from flask_restful import Resource, reqparse
from api import models
from api.database import db
from sqlalchemy.sql import text
from datetime import datetime
from sqlalchemy import select


class Clima(Resource):
    def get(self):   
        parser = reqparse.RequestParser()
        parser.add_argument('name')        
        args = parser.parse_args()
        city_filter = args['name']
        results = db.query( models.Temperature, models.City).join('city').filter_by(name=city_filter).all()
        data = []
        for row in results:
            temp = row[0].to_dict()
            city = row[1].to_dict()
            temp['name'] = city['name']
            data.append(temp)
        return data
    def post(self):
        pass
class Cities(Resource):
    def get(self):
        cities = db.query(models.City).all()
        return cities

