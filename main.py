from flask import Flask, request


app = Flask(__name__)

@app.route("/",methods=['GET'])

def validation_page():
    name = str(request.args['https://miathemileresume.herokuapp.com/'])
    return name


if __name__ == '__main__':
    app.run(debug=True)