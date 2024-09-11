from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess(name):
    agify_response = requests.get(f"https://api.agify.io?name={name}")
    age = agify_response.json()["age"]

    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = genderize_response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)