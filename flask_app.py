from flask import Flask, request, render_template, jsonify
from functions import *

app = Flask(__name__)


@app.route('/frame')
def frame():
    return jsonify(randomFrame(request.args['d']))


@app.route('/')
def main():
    return render_template('index.html', debug=False)


@app.route('/debug')
def main2():
    return render_template('index.html', debug=True)


if __name__ == '__main__':
    app.run()
