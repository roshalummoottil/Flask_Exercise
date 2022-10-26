from datetime import date
from urllib import request
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
global studentOrganizationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails ={"Rosh": "The Boxing Academy", "Josh": "The Master Grapplers", "Andrew": "The Jiu Jitsu Gym", "David": "The Judo Mat", "Kai": "The Muay Thai Club"}



@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.now()
    return render_template('index.html', currentDate = currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
     # Write your to code here to check whether number is even or odd and render result.html page
    if number == "":
        return render_template('result.html', number = "No number provided")
    if number.isdigit():
        if int(number)%2 == 0:
            return render_template('result.html', number = number + " is an even number")
        else:
            return render_template('result.html', number = number + " is an odd number")
    else:
        return render_template('result.html', number = "The provided input is not an integer!") 
        
    

@app.get('/addStudentOrganization')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/studentdetails', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['sname']
    organisation = request.form['organization']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName]= organisation

    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)