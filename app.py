from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client 
import random

app = Flask(__name__)
api_key = "10895faad0msh9814694d667c167p1a1faajsn7513ea6fdb5f"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///epass.db' 
#It is used to mention the path where the database is stored.///(from where this file is there) is relative path //// is absolute path(from root).

db=SQLAlchemy(app) 

'''
account_sid = 'sid key' 
auth_token = 'token' 
'''

#client = Client(account_sid, auth_token) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
class login_data(db.Model):
    id_no=db.Column(db.Integer,primary_key=True) #Captial C for Columns
    username=db.Column(db.Text,nullable=False)
    email=db.Column(db.Text,nullable=False)
    mobilenumber=db.Column(db.Text,nullable=False)
    password=db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"login_data('{self.username}','{self.email}','{self.mobilenumber}')"
    
class Appointment_request(db.Model):
    id_no=db.Column(db.Integer,primary_key=True) #Captial C for Columns
    name=db.Column(db.Text,nullable=False)
    email=db.Column(db.Text,nullable=False)
    contactnumber=db.Column(db.Text,nullable=False)
    Appointment_description=db.Column(db.String(60),nullable=False)
    date=db.Column(db.Text,default="n/a")
    time=db.Column(db.Text,default="n/a")
    status=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"Appointment_request('{self.name}','{self.email}','{self.contactnumber}')"

    

'''
Home route
'''
@app.route("/")
def home():
    pass
    

'''
Login route
'''
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        u_name=request.form['name']
        email=request.form['email']
        m_number=request.form['mnumber']
        p_pass=request.form['purpose']
        rand=random.randint(1578935478963,5555555555555) 

'''
Appointmentrequest route
'''
@app.route("/appointmentrequest",methods=['POST','GET'])
def appointmentrequest():
    if request.method == 'POST':
        u_name=request.form['name']
        email=request.form['email']
        m_number=request.form['mnumber']
        appoint_d=request.form['description']
        date=request.form['date']
        time=request.form['time']
    
    

if __name__ == "__main__":
    app.run(debug=True)