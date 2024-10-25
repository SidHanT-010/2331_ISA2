#app.py
from flast import Flask
app=Flask(__name__)

@app.route("/")
def rollno():
		return "rollno:2331"
