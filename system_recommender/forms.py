from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProfileUpdateForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    username = TextAreaField('Username', validators=[DataRequired()])
    user_preferences = TextAreaField('Preferences')
    movies_watched = TextAreaField('Watch_History')
    submit = SubmitField('Update Profile')