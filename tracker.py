import csv
#want to use flask 
from flask import Flask,render_template, request, redirect
#create my website
app = Flask(__name__)



#Home route,
#connect to index.html
#shows the first page of the website
#app stores the website, '/'IS THE WEBSITE ADDRESS
@app.route("/")
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

   #Open the file called glucose_reading.csv. "a" add info to the bottom
   #do not erase the old
    with open("glucose_reading.csv", "a" , newline ="") as file:
        #This creates a special CSV-writing tool
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


    #calculate the average stats and general stats
    if glucose_values:
        average = round(sum(glucose_values) / len(glucose_values) , 1)
        highest = max(glucose_values)
        lowest = min(glucose_values)
    else:
        average = 0
        highest = 0
        lowest = 0

    #display the readings
    return render_template("data.html", readings=readings,
                           dates = dates,
                            glucose_values= glucose_values,
                            average = average,
                            highest = highest,
                            lowest = lowest)

    
#delete route
#for deleting readings
#displayed on data page
@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    with open("glucose_reading.csv","r") as file:
        #create a reader thst read through each file,
        # (list) give you the whole list
        rows = list(csv.reader(file))
    row = [row for row in rows if row]
    rows.pop(index + 1)

    #ease everything inside the row
    with open("glucose_reading.csv", "w", newline ="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    return redirect("/data")
              
              
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)

