from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def new():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)