from flask import Flask, request, render_template, jsonify
from functions import *

app = Flask(__name__)


@app.route('/frame')
def frame():
    return jsonify(randomFrame(request.args['d']))


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
