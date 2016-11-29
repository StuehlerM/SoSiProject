from flask import Flask
from flask import g
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Config as config
from Presenter import Presenter

Session = sessionmaker(expire_on_commit = False)
Engine = create_engine('mysql://' +
                        config.MYSQL_DATABASE_USER +
                        ':' +
                        config.MYSQL_DATABASE_PASSWORD +
                        '@' +
                        config.MYSQL_DATABASE_HOST +
                        ':' +
                        str(config.MYSQL_DATABASE_PORT) +
                        '/' +
                        config.MYSQL_DATABASE_DB +
                        '?charset=utf8&use_unicode=1'
                        )

app = Flask(__name__)
app.config.from_pyfile("Config.py")

@app.before_request
def beforeRequest():
    g.presenter = Presenter(Session)

@app.route("/", methods=['GET', 'POST'])
def landingpage():
        p = g.get("presenter")
        if isinstance(p, Presenter):
            return p.handleDefault()
        return "Error - you know what you did wrong I guess?"

@app.route("/login", methods=['POST'])
def login():
        p = g.get("presenter")
        if isinstance(p, Presenter):
            return p.handleLogin()
        return "Error - you know what you did wrong I guess?"

@app.route("/logout", methods=['POST'])
def logut():
        p = g.get("presenter")
        if isinstance(p, Presenter):
            return p.handleLogout()
        return "Error - you know what you did wrong I guess?"

@app.route("/register", methods=['POST'])
def register():
    p = g.get("presenter")
    if isinstance(p, Presenter):
        return p.handleRegister()
    return "Error - you know what you did wrong I guess?"

@app.route("/registerForm", methods=['GET', 'POST'])
def registerForm():
        return render_template("Register.html", titleExt= "Registrierung")

@app.route("/booking", methods=['POST'])
def booking():
        p = g.get("presenter")
        if isinstance(p, Presenter):
            return p.handleBooking()
        return "Error - you know what you did wrong I guess?"

if __name__ == "__main__":
        app.run()