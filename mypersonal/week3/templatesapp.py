from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("index.html", name="This is change")

@app.route("/newtemplates")
def newtemplates():
    return render_template("page.html")

@app.route("/newtemplate")
def newtemplate():
    return render_template("newtemplate.html")


@app.route("/submit", methods=["GET" , "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")

# Home page
@app.route("/")
def home():
    return "Python is installed in Flask"


# Index template
@app.route("/template")
def templates():
    return render_template("index.html", name="Bidhan")


if __name__ == "__main__":
    app.run(debug=True)







