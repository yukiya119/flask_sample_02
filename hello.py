from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


if __name__ == '__main__':
    hostname = "127.0.0.1"
    port = 5000
    app.run(host=hostname, port=port, debug=True)
