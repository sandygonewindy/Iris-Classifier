from flask import Flask, render_template, request
import model
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods = ["POST"])
def classify():
    feature_1 = request.form["s-length"]
    feature_2 = request.form["s-width"]
    feature_3 = request.form["p-length"]
    feature_4 = request.form["p-width"]
    species = model.result(feature_1, feature_2, feature_3, feature_4)
    return render_template("classify.html", species = species)
if(__name__ == "__main__"):
    app.run()