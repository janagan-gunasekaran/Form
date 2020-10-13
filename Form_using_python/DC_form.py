
from flask import Flask, render_template, url_for, flash, redirect, request,Response
import json
import requests
from werkzeug.utils import secure_filename
from datetime import datetime
original_data = []



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")

@app.route("/DC_form", methods=['GET', 'POST'])
def DC_form():
    if request.method == "POST":
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        mobile = request.form['mobile']
        dob = request.form['dob']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        email = request.form['country']
        file = request.files['file']
        file_name = secure_filename(file.filename)
        file_path = 'C:/Users/HOME/Desktop/Janagan Portfolio/Test_to_new_files/' + file_name
        # file.save(file_path)
        # print(name,username,email,confirm_password,mobile,dob,address,city,state,email,file,sep='\n')
        original_data1 = []
        original_data1.append(name)
        original_data1.append(email)
        original_data1.append(mobile)
        original_data1.append("Pending")
        original_data.append(original_data1)
        print(original_data)
        return redirect(url_for('DC_form_table' ))

    return render_template('DC_form.html',title='DC_form')

@app.route("/DC_form_table", methods=['GET', 'POST'])
def DC_form_table():
    
    return render_template('DC_form_table.html',title='DC_form_table',original_data=original_data)

  

if __name__ == '__main__':
    app.run(debug=True)




    