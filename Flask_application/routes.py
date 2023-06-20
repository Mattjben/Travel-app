
from flask import Flask, render_template, request, redirect, url_for,flash,session
from Flask_application import app
import pandas as pd

#------------------------------------------------------------------------------------
# HomePage - website info 
#------------------------------------------------------------------------------------
@app.route('/')
@app.route('/Home')
def root_route():
   exampletable = pd.read_excel(r'Flask_application\static\Sampletable.xlsx')
   table_html = exampletable.to_html(table_id="table", classes='table table-light table-striped-columns')
   return render_template('Home.html',title="Travel Data Input",table=table_html)

