from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon premier projet CI/CD avec Docker et GitHub Actions devops1 !"


@app.route("/About")
def about():
    return "À propos de mon projet CI/CD avec Docker et GitHub Actions !(MY SECOND PAGE OF MY PROJECT)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)