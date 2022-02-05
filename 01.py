from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


@app.route("/login", methods=["Get", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        return "Login!"


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
