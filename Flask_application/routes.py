
from flask import Flask, render_template, request, redirect, url_for,flash,session,send_from_directory
from Flask_application import app
from flask_wtf.csrf import CSRFProtect
from Flask_application.Forms import FileForm,downloadForm
import pandas as pd
from datetime import datetime

import os

app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)
app.config['DOWNLOAD_FOLDER'] = os.path.join(app.root_path, 'static')
# Global variable to store the DataFrame

#------------------------------------------------------------------------------------
# HomePage - website info 
#------------------------------------------------------------------------------------
@app.route('/')
@app.route('/import', methods=['GET', 'POST'])
def root_route():
   form = FileForm()

   if form.validate_on_submit():
      file = form.file.data

      try:
         global_df  = pd.read_excel(file)
         # Do something with the data, such as saving to a database
         # or performing calculations
         df_html = global_df.to_html()
         if global_df is not None:
            # Define the file path
            filename = 'Finance_Report'
            filepath = os.path.join(app.root_path, 'static', filename)
            # Save the dataframe as a CSV file
            global_df.to_csv(filepath, index=False)
         download_form = downloadForm()
         # Return a success message
         return render_template('Dashboard_main.html', data=df_html,form=download_form)
    
      except Exception as e:
         return f'Error importing file: {str(e)}'
   else:
      current_directory = os.path.dirname(__file__)
      file_path = os.path.join(current_directory, "static", "Sampletable.xlsx")
      exampletable = pd.read_excel(file_path)
      table_html = exampletable.to_html(table_id="table", classes='html-table')
      return render_template('Home.html',title="Travel Data Input",table=table_html,form=form)
 
@app.route('/download', methods=['GET', 'POST'])
def download():
      if request.method == 'POST':
         filename = 'Finance_Report.csv'
         return send_from_directory(app.config['DOWNLOAD_FOLDER'], r"{}".format(filename), as_attachment=True)
  
      
              

       

