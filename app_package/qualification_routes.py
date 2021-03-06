from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
from app_package.qualification_forms import DisplayQualificationForm,AddQualificationForm,QualificationForm
from app_package.course_forms import AddCourseForm


qual_id=0
check=True
@app.route("/add_qualification",methods=["GET","POST"])
def add_qualification():
	global qual_id,check
	form=QualificationForm()
	course_col=mongo.db.courses
	qual_col=mongo.db.qualification
	cqual_col=mongo.db.course_qualification
	cour=course_col.find()
	lst=[]
	for q in cour:
		lst.append((q['courseName'],q["courseName"]))
	form.courseName.choices=lst
	if form.validate_on_submit():
		form=AddQualificationForm()
		allqual=cqual_col.find({"courseName":form.courseName.data})
		qual=qual_col.find()
		lst=[]
		for q in qual:
			lst.append((q['qualname'],q["qualname"]))
		form.qualname.choices=lst
		return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
		
	return render_template("selectqualification.html",form=form,course=form.courseName.data)


@app.route("/view_qualification",methods=["GET","POST"])
def view_qualification():
	global qual_id
	global check
	form=AddQualificationForm()
	fields=["_id","courseName","qualname"]
	cqual_col=mongo.db.course_qualification
	if check:
		check=False
		if cqual_col.count()==0:
			qual_id=0
		else:
			cqual=cqual_col.find().sort("_id",-1).limit(1)
			tmp=cqual.next()
			qual_id=tmp["_id"]
	qual_id+=1	
	values=[qual_id,form.courseName.data,form.qualname.data]
	cqual=dict(zip(fields,values))
	crs_qual=cqual_col.find({"courseName":form.courseName.data})
	flag=True
	for i in crs_qual:
		if i['qualname']==form.qualname.data:
			flag=False
			break
		else:
			flag=True
	qual_col=mongo.db.qualification
	allqual=cqual_col.find({"courseName":form.courseName.data})
	qual=qual_col.find()
	lst=[]
	for q in qual:
		lst.append((q['qualname'],q['qualname']))
	#form=AddQualificationForm
	form.qualname.choices=lst
	if flag:
		temp=cqual_col.insert_one(cqual)
		if temp.inserted_id==qual_id:
			flash("Qualification added")
			return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
		else:
			flash("problem on adding qualification")
			return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)
	else:
		flash("Qualification already exists")
		return render_template("addqualification.html",allqual=allqual,form=form,course=form.courseName.data)


@app.route("/deletequalification/<int:a>/<string:b>", methods=["GET","POST"])
def deletequalification(a,b):
    form=AddQualificationForm()
    cqual_col=mongo.db.course_qualification
    cqual_col.delete_one({"_id":a})
    qual_col=mongo.db.qualification
    allqual=cqual_col.find({"courseName":b})
    qual=qual_col.find()
    lst=[]
    for q in qual:
        lst.append((q['qualname'],q["qualname"]))
    form.qualname.choices=lst
    flash("Qualification deleted")
    return render_template("addqualification.html",allqual=allqual,form=form,course=b)    
        
	
