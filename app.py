import pprint
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    pprint.pprint(request.json)

    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		    'body': request.json
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8260, debug=True)