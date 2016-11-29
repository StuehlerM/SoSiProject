from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_pyfile("Config.py")


@app.route("/", methods=['GET', 'POST'])
def landingpage():
        return render_template("ParentTemplate.html", titleExt = "4U")

@app.route("/login", methods=['POST'])
def login():
        return "Nicht hello world"

@app.route("/logout", methods=['POST'])
def logut():
        return "Nicht hello world"

@app.route("/register", methods=['GET'])
def register():
        return "Nicht hello world"

@app.route("/booking", methods=['POST'])
def booking():
        return "Nicht hello world"

if __name__ == "__main__":
        app.run()