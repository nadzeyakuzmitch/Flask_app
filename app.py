from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    # Redirect to an external website, e.g., "https://www.example.com"
    return redirect("https://flask.palletsprojects.com/en/3.0.x/")

if __name__ == '__main__':
    app.run(host='0.0.0.0')