from flask import Flask
from flask_restful import Api,Resource
from nutrition import *
from flask import jsonify
app = Flask(__name__)
api = Api(app)

@app.route("/<int:age>/<string:gen>/<string:pref>", methods=['GET'])
def nutrition(age,gen,pref):
    js = start(age,gen,pref)
    result=[]
    for i in js:
    	result.append(i)
    return jsonify(result)


if __name__ == '__main__':
	app.run(debug=True)
