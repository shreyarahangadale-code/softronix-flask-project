from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/content")
def content():
    return "<h1>Welcome to Softtronix IT Training</h1>"

@app.route("/soft")
def soft():
    return "<marquee> <h1> Softtronix IT Training...</h1> </marquee>"


if __name__ == "__main__":
    app.run(debug=True)
