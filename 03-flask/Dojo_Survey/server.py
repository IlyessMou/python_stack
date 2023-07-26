from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret-key"  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        return redirect(url_for("result"))
    return render_template("index.html")

@app.route("/result")
def result():
    name = session.get("name")
    location = session.get("location")
    language = session.get("language")
    comment = session.get("comment")
    return render_template("result.html", name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
