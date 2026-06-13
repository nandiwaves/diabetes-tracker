#want to use flask 
from flask import Flask,render_template
#create my website
app = Flask(__name__)
#app stores the website, '/'IS THE WEBSITE ADDRESS
@app.route("/")
#Show the file you just wrote
def home():
    return render_template("index.html")
@app.route("/add")
def add():
    return"<h1> Readings Page</h1>"
if __name__ == "__main__":
    app.run(debug=True, port=5001)

