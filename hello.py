from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    return "login!!"


if __name__ == '__main__':
    hostname = "127.0.0.1"
    port = 5001
    app.run(host=hostname, port=port, debug=True)
