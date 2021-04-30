from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email 


class UploadForm(FlaskForm):
    Description=TextAreaField('Description',validators=[DataRequired()]) 
    Photo=FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
