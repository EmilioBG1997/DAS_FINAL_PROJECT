from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heroes")
def DcHeroes():
    return render_template("heroes.html")

@app.route("/heroes/<hero>")
def Hero(hero):
    return render_template("hero.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    