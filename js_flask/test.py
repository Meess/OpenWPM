from flask import Flask, current_app
app = Flask(__name__)

@app.route("/")
def hello():
    return current_app.send_static_file('jsapi.html')

@app.route("/jsapi.js")
def js():
	return current_app.send_static_file('jsapi.js')

if __name__ == "__main__":
    app.run()