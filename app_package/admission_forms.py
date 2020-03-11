from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,ValidationError,Length,Email,NumberRange
from wtforms.validators import Regexp
from wtforms.fields.html5 import EmailField

class AddAdmissionForm(FlaskForm):
    e_name=StringField("Name: ",validators=[DataRequired(message="Enter Your Name")])
    e_age=IntegerField("Age: ",validators=[DataRequired(message="Enter Your Age"),NumberRange(min=1,max=80,message="Please enter valid age")])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_qualification=SelectField("Qualification: ",[DataRequired(message="Please select an option")],choices=[('B Tech', 'B Tech'), ('M Tech', 'M Tech'), ('MCA', 'MCA')])
    e_phone=StringField("Mobile no", validators=[DataRequired(message="Enter Your Phone Number"),Length(min=10, max=10,message="Please enter corect value")])
    e_passout_year=IntegerField("Year of passout : ",validators=[DataRequired(message="Enter Your Year of Passout"),NumberRange(min=1990,max=2020,message="Please enter corect value")])
    e_email=EmailField("Email: ",validators=[DataRequired(message="Enter Your Email Id"),Email("Please enter your email address.")])
    e_course=SelectField("Course: ",[DataRequired(message="Please select an option")],choices=[('Python', 'Python'), ('Java', 'Java'), ('Testing', 'Testing')])
    e_batch=IntegerField("Batch Assigned:",validators=[DataRequired()])
    e_guardianname=StringField("Guardian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Register")


class AdmissionSearchForm(FlaskForm):
    e_phone=StringField("Phone:",validators=[DataRequired()])
    submit=SubmitField("Search")

class UpdateAdmissionForm(FlaskForm):
    e_age=IntegerField("Age: ",validators=[DataRequired(message="Enter Your Age"),NumberRange(min=0,max=80,message="Please enter valid age")])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_qualification=SelectField("Qualification: ",[DataRequired(message="Please select an option")],choices=[('B Tech', 'B Tech'), ('M Tech', 'M Tech'), ('MCA', 'MCA')])
    e_phone=StringField("Mobile no", validators=[DataRequired(message="Enter Your Phone Number"),Length(min=10, max=10,message="Please enter corect value")])
    e_passout_year=IntegerField("Year of passout : ",validators=[DataRequired(message="Enter Your Year of Passout"),NumberRange(min=1990,max=2020,message="Please enter corect value")])
    e_email=EmailField("Email: ",validators=[DataRequired(message="Enter Your Email Id"),Email("Please enter your email address.")])
    e_course=SelectField("Course: ",[DataRequired(message="Please select an option")],choices=[('Python', 'Python'), ('Java', 'Java'), ('Testing', 'Testing')])
    e_batch=StringField("Batch Assigned:",validators=[DataRequired()])
    e_guardianname=StringField("Guardian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Update Details ")

    

