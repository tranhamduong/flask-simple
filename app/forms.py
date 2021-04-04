from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    name = StringField('Name:', validators=[InputRequired()])
    phone_number = StringField('Phone Number:', validators=[InputRequired()])
    image = StringField('Avatar Image URL:', validators=[InputRequired()])

class LookupForm(FlaskForm):
    phone_number = StringField('Phone Number:', validators=[InputRequired()])
    
class JackpotForm(FlaskForm):
    phone_number = StringField('Phone Number:', validators=[InputRequired()])
    jackpot_keys = StringField('Phone Number:', validators=[InputRequired()])