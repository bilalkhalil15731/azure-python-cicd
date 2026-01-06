from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Hello World logged from Azure!")
    return "Hey everyone! This is Azure CI/CD Pipeline!"

if __name__ == "__main__":
    app.run()
