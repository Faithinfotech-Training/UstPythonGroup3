from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired,EqualTo,ValidationError

class AddCourseForm(FlaskForm):
    courseId=IntegerField("CourseId: ",validators=[DataRequired()])
    courseName=StringField("CourseName: ",validators=[DataRequired()])
    courseDuration=StringField("Courseduration: ",validators=[DataRequired()])
    courseFee=IntegerField("Course Fee: ",validators=[DataRequired()])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired()])
    courseStatus=RadioField("CourseStatus: ",choices=[("active","active"),("inactive","inactive")])
    submit=SubmitField("Add Course")
    
class ModifyCourseForm(FlaskForm):
    courseName=StringField("CourseName: ",validators=[DataRequired()])
    courseDuration=StringField("CourseDuration: ",validators=[DataRequired()])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired()])
    courseFee=IntegerField("Course Fee: ",validators=[DataRequired()])
    courseStatus=RadioField("CourseStatus: ",choices=[("active","active"),("inactive","inactive")])
    submit=SubmitField("Update Course")
    

