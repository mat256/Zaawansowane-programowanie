from flask import Flask
from flask_restful import Resource, Api
from modules.dane import data_new
#import modules.movies

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Movies(Resource):
    def get(self):
        return data_new('modules/movies.csv')

class Ratings(Resource):
    def get(self):
        return data_new('modules/ratings.csv')

class Links(Resource):
    def get(self):
        return data_new('modules/links.csv')

class Tags(Resource):
    def get(self):
        return data_new('modules/tags.csv')

api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Ratings, '/ratings')
api.add_resource(Links, '/links')
api.add_resource(Tags, '/tags')


if __name__ == '__main__':
    app.run(debug=True)