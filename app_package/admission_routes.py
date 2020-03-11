from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
from flask_login import current_user,login_user,logout_user,login_required
from app_package.admission_forms import AdmissionSearchForm,AddAdmissionForm,UpdateAdmissionForm

admission_id=0
check1=True
@app.route("/add_admission",methods=["GET","POST"])
def add_admission():
    global admission_id
    global check1
    form=AddAdmissionForm()
    if form.validate_on_submit():
        admission_col=mongo.db.admission
        if check1:
            check1=False
            if admission_col.count()==0 :
               admission_id=0
            else:
                enq=admission_col.find().sort("_id",-1).limit(1)
                tmp=enq.next()
                admission_id=tmp["_id"]
            admission_id+=1
            fields=["_id","e_name","e_age","e_gender","e_qualification","e_phone","e_passout_year","e_email","e_course","e_batch","e_guardianname","e_guardianphone","e_address"]
        e_gender = dict(form.e_gender.choices).get(form.e_gender.data)
        values=[admission_id,form.e_name.data,form.e_age.data,e_gender,form.e_qualification.data,form.e_phone.data,form.e_passout_year.data,form.e_email.data,form.e_course.data,form.e_batch.data,form.e_guardianname.data,form.e_guardianphone.data,form.e_address.data]
        admissions=dict(zip(fields,values))
        tmp=admission_col.insert_one(admissions)
        if tmp.inserted_id==admission_id:
            flash(" Candidate Added")
            return redirect(url_for("admission_display"))
        else:
            flash("Problem in adding Candidate")
            return redirect(url_for("add_admission"))
    else:
        return redirect(url_for("add_admission"))

@app.route("/admission_search",methods=["GET","POST"])
def admission_search():
    form=AdmissionSearchForm()
    
    if form.validate_on_submit():
        admission_col=mongo.db.enquiries
        edata=admission_col.find_one({"phone":form.e_phone.data})
        #if edata["status"]=="Exam Passed":
        form=AddAdmissionForm()
        
        return render_template("add_admission.html",form=form,edata=edata)
       
        #else:
            #flash("Not Applicable Student")
            #return redirect(url_for("admission_search"))
    else:
         return render_template("admission_search.html",form=form)
      



@app.route("/update_admission/<int:a_id>",methods=["GET","POST"])
def update_admission(a_id):
    form=UpdateAdmissionForm()
    admission_col=mongo.db.admission
    data=admission_col.find_one({"_id":a_id})
    if form.validate_on_submit():
        values=dict()
        e_gender = dict(form.e_gender.choices).get(form.e_gender.data)
        e_course=dict(form.e_course.choices).get(form.e_course.data)
        e_qualification=dict(form.e_qualification.choices).get(form.e_qualification.data)
        values["e_age"]=form.e_age.data
        values["e_gender"]=e_gender
        values["e_qualification"]=e_qualification
        values["e_phone"]=form.e_phone.data
        values["e_passout_year"]=form.e_passout_year.data
        values["e_email"]=form.e_email.data
        values["e_course"]=e_course
        values["e_batch"]=form.e_batch.data
        values["e_guardianname"]=form.e_guardianname.data
        values["e_guardianphone"]=form.e_guardianphone.data
        values["e_address"]=form.e_address.data
        new_data={"$set":values}
        query={"_id":a_id}
        admission_col.update_one(query,new_data)
        flash("Candidate details modified")
        return redirect(url_for("admission_display"))
    else:
        return render_template("update_admission.html",form=form,data=data)

@app.route("/admission_display")
def admission_display():
    admission_col=mongo.db.admission
    admission=admission_col.find()
    return render_template("admission_display.html",admission=admission)
    
@app.route("/admission")
def admission():
    return render_template("admission.html")    
    
    
