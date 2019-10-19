import pandas as pd
import xlrd
import mysql.connector
from sqlalchemy import create_engine
from flask import Flask, render_template, url_for, request

engine = create_engine('mysql://@localhost/sample')

app = Flask(__name__)

@app.route("/")
@app.route("/home",  methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
       select = request.form.get('comp_select')
       print(select)
       if select == '1':
           return render_template('insert.html')
       elif select == '2':
           return render_template('delete.html')
       elif select == '3':
           return render_template('fastest.html')
       elif select == '4':
           return render_template('strongest.html')
       elif select == '5':
           return render_template('view.html')
    return("Error selecting option. Try Again")


if __name__ == '__main__':
    app.run(debug=True)
