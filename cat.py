from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>THIS IS A CAT</h1><div style="font-size: 10em">🐱</div>'
