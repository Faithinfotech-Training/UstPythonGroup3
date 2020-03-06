from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
#from flask_login import current_user,login_user,logout_user,login_required
from app_package.course_forms import AddCourseForm,ModifyCourseForm

check=True    
co_id=0
@app.route("/menu",methods=["GET"])
def menu():

    return render_template("menu.html")
    
@app.route("/course")
def course():
    return render_template("course.html")
    
@app.route("/addcourse",methods=["GET","POST"])
def addcourse():
    global co_id
    global check
    form=AddCourseForm()
    if form.validate_on_submit():
        fields=["_id","courseId","courseName","","courseDuration","courseFee","courseDescription","courseStatus"]
        course_col=mongo.db.courses
        if check:
            check=False
            if course_col.count()==0:
                co_id=0
            else:
                cou=course_col.find().sort("_id",-1).limit(1)
                tmp=cou.next()
                co_id=tmp["_id"]
        co_id+=1
        values=[co_id,form.courseId.data,form.courseName.data,form.courseDuration.data,form.courseFee.data,form.courseDescription.data,form.courseStatus.data]
        course=dict(zip(fields,values))
        temp=course_col.insert_one(course)
        if temp.inserted_id==co_id:
            flash("course added")
            return redirect(url_for("menu"))
        else:
            flash("problem on adding course ")
            redirect(url_for("addcourse"))
    else:
        return render_template("addcourse.html",form=form)
        
        

@app.route("/modifycourse/<int:a>",methods=["GET","POST"])
def modifycourse(a):
    form=ModifyCourseForm()
    
    if form.validate_on_submit():
        values=dict()
        course_col=mongo.db.courses
        
        if form.courseName.data!="":values["courseName"]=form.courseName.data
        if form.courseFee.data!="":values["courseFee"]=form.courseFee.data
        if form.courseDuration.data!="":values["courseDuration"]=form.courseDuration.data
        if form.courseDescription.data!="":values["courseDescription"]=form.courseDescription.data
        if form.courseStatus.data!="":values["courseStatus"]=form.courseStatus.data
        query={"_id":a}
        new_data={"$set":values}
        course_col.update_one(query,new_data)
        flash("Course Modified")
        return redirect(url_for('course'))
    else:
        return render_template("modifycourse.html",form=form)
    
@app.route("/viewcourses",methods=["GET","POST"])
def viewcourses():
    course_col=mongo.db.courses
    courses=course_col.find()
   
    return render_template("allcourses.html",courses=courses)
  
    
    
    
    
    
    
    
    
    