from wtforms import StringField, PasswordField, BooleanField, FormField, SubmitField, TextAreaField, validators, Form
from wtforms.fields.simple import EmailField
from wtforms.validators import InputRequired, EqualTo


class SignUpUserForm(Form):
    first_name = StringField('first_name', validators=[InputRequired(), validators.Length(min=2)])
    last_name = StringField('last_name', validators=[InputRequired(), validators.Length(min=2)])
    email = EmailField('email', validators=[InputRequired(), validators.email()])
    address = StringField('address', validators=[InputRequired()])
    phone = StringField('phone', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    confirm_password = PasswordField('confirm_password', validators=[InputRequired(), EqualTo('password', 'Password and Password Confirmaton must match')])

