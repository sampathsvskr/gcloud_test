from flask import Flask
import os

app=Flask(__name__)


@app.route('/')
def hello():	
	return "Welcome to Dockerized app version 2"


if __name__=="__main__":
	app.run(host="0.0.0.0",debug=True, port=int(os.environ.get("PORT", 8080)))