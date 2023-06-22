from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms import SubmitField, FileField

class FileForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Submit')

class downloadForm(FlaskForm):
    submit = SubmitField('Download CSV')
