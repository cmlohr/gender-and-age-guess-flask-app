import flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def name(name):
    age_request = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_request.json()["age"]
    gender_request = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_request.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)