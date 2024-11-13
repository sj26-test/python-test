from flask import Flask
from python_test_dependency import buildkite

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, {buildkite()}!</p>"

if __name__ == "__main__":
    app.run()
