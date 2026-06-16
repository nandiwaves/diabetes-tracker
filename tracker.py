import csv
#want to use flask 
from flask import Flask,render_template, request, redirect
#create my website
app = Flask(__name__)
#app stores the website, '/'IS THE WEBSITE ADDRESS
@app.route("/")
#Show the file you just wrote


#Home route,
#connect to index.html
#shows the first page of the website
def home():
    return render_template("index.html")


#Add route
#connects add.html
#shows the form where the user enters
# a glucose reading
@app.route("/add")
def add():
    return render_template("add.html")

#save route
#connects from form in add.html
#receives form data and saves it 
# into the CSV file
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
    


# data route
# Connects to: templates/data.html
# Purpose: reads saved CSV data 
# and displays it on the webpage
@app.route("/data")
def data():
    #store all the glucose reading
    readings = []
    dates =[]
    glucose_values =[]
    #open the cvs file in read mode 
    with open("glucose_reading.csv", "r") as file:
        #create a csv reader
        reader =csv.reader(file)
        #add each row to the reading list
        next(reader)
        for row in reader:
            if len(row) < 3 or row[2] == "":
                continue
            readings.append(row)
            dates.append(row[0])
            glucose_values.append(int(row[2]))
    #display the readings
    return render_template("data.html", readings=readings,
                           dates = dates,
                            glucose_values= glucose_values)

   
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)

