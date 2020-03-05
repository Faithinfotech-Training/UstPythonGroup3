from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired,EqualTo,ValidationError
from app_package.models import User
