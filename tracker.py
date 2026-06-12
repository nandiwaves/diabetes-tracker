#want to use flask 
from flask import Flask,render_template
#create my website
app = Flask(__name__)
#app stores the website, '/'IS THE WEBSITE ADDRESS
@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

