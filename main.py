from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def validation_page():
    name = str(request.args['name'])
    return name


if __name__ == '__main__':
    app.run(debug=True)