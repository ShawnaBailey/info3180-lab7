from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    description = TextAreaField("Enter Description", validators=[DataRequired()])
    photo = FileField("Upload Image", validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg', 'Images only!'])
        ])