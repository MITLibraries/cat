from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return '<div style="font-size: 10em">🐱</div>'
