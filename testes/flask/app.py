from flask import Flask

app = Flask("flask")


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200


app.run(debug=True, use_reloader=True)

