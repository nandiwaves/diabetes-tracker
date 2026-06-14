import csv
#want to use flask 
from flask import Flask,render_template, request, redirect
#create my website
app = Flask(__name__)
#app stores the website, '/'IS THE WEBSITE ADDRESS
@app.route("/")
#Show the file you just wrote
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/save", methods=["POST"])
def save():
    #get values entered by the user
    date = request.form["date"]
    time = request.form["time"]
    glucose = request.form["glucose"]
   
    with open("glucose_reading.csv", "a" , newline ="") as file:
        writer = csv.writer(file)
        writer.writerow([date, time, glucose])
        #take user to user data page
        return redirect("/data")
    

@app.route("/data")
def data():
    #store all the glucose reading
    readings = []
    #open the cvs file in read mode 
    with open("glucose_reading.csv", "r") as file:
        #create a csv reader
        reader =csv.reader(file)
        #add each row to the reading list
        for row in reader:
            readings.append(row)
    #display the readings
    return render_template("data.html", readings=readings)
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)

