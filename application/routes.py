from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index="active")

@app.route("/dungeon")
def dungeon():
    return render_template("dungeon.html", dungeon="active")

@app.route("/room")
def room():
    return render_template("room.html", room="active")

@app.route("/map")
def map():
    return render_template("map.html", map="active")

@app.route("/monsters")
def monsters():
    return render_template("monsters.html", monsters="active")

@app.route("/treasure")
def treasure():
    return render_template("treasure.html", treasure="active")