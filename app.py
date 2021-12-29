from flask import Flask
from flask_restful import Api,Resource
from nutrition import *
from flask import jsonify
app = Flask(__name__)
api = Api(app)

@app.route("/<int:age>/<string:gen>/<string:pref>", methods=['GET'])
def nutrition(self,age,gen,pref):
    js = start(age,gen,pref)
    return js

# class nutrition(Resource):
# 	def get(self,age,gen,pref):
# 		js = start(age,gen,pref)
# 		return js
# api.add_resource(nutrition,"/nutrition/<int:age>/<string:gen>/<string:pref>")

if __name__ == '__main__':
	app.run(debug=True)
