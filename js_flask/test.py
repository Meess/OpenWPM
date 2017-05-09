from flask import Flask, current_app
app = Flask(__name__)

@app.route("/")
def hello():
    return current_app.send_static_file('jsapi.html')

@app.route("/static/apicalls/<file>")
def js():
	return current_app.send_static_file('/static/apicalls/' + file)

if __name__ == "__main__":
    app.run()