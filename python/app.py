from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Val after adding pwd to github actions new try!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
