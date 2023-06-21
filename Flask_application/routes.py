
from flask import Flask, render_template, request, redirect, url_for,flash,session
from Flask_application import app
import pandas as pd
import os

#------------------------------------------------------------------------------------
# HomePage - website info 
#------------------------------------------------------------------------------------
@app.route('/')
@app.route('/Home')
def root_route():
   current_directory = os.path.dirname(__file__)
   file_path = os.path.join(current_directory, "static", "Sampletable.xlsx")
   exampletable = pd.read_excel(file_path)
   table_html = exampletable.to_html(table_id="table", classes='table table-light table-striped-columns')
   return render_template('Home.html',title="Travel Data Input",table=table_html)

