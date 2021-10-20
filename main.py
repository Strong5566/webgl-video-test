from flask import Flask, render_template
import flask
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route("/")
def home():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return render_template("index.html", some_var=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
