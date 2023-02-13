from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

if __name__ == "__main__":
    app.run(debug = True)