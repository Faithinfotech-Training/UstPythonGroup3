from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired,EqualTo,ValidationError

class AddCourseForm(FlaskForm):
    courseId=InegerField("CourseId: ",validators=[DataRequired()])
    courseName=StringField("CourseName: ",validators=[DataRequired()])
    courseDuration=StringField("Courseduration: ",validators=[DataRequired()])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired()])
    courseStatus=StringField("CourseStatus: ",validators=[DataRequired()])
    submit=SubmitField("Add Course")
    
class ModifyCourseForm(FlaskForm):
    courseId=InegerField("CourseId: ",validators=[DataRequired()])
    courseDuration=StringField("Courseduration: ",validators=[DataRequired()])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired()])
    courseStatus=StringField("CourseStatus: ",validators=[DataRequired()])
    submit=SubmitField("Update Course")
    
class HideCourseForm(FlaskForm):
    courseStatus=StringField("CourseStatus: ",validators=[DataRequired()])
    submit=SubmitField("Update")
