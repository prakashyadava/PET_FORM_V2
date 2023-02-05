from flask import Flask,render_template,redirect,url_for
from allPetConn import *
from petForm import *
from log import Log
app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret_key"
@app.route('/',methods=['GET','POST'])
def home():
    return render_template("pet_home_page.html")

@app.route('/pet_data',methods = ['GET','POST'])
def pet_records():
    data = None
    DBConnection.connect_db()
    data =DBConnection.display_records()
    DBConnection.close_db()
    if data==None:
        return render_template("table_not_found.html")
    if len(data)==0:
        return render_template("empty_record.html")
    return render_template("pet_display.html",data=data)

@app.route('/delete_data/<pet_id>',methods=['GET','POST'])
def delete_data(pet_id):
    DBConnection.connect_db()
    DBConnection.delete_row(int(pet_id))
    DBConnection.close_db()
    return redirect(url_for('pet_records'))
@app.route('/modify_data/<pet_id>',methods = ['GET','POST'])
def modify_data(pet_id):
    DBConnection.connect_db()
    form = UpdateForm()
    form.pet_id.data = pet_id 
    if form.validate_on_submit():
        DBConnection.update_data(int(form.pet_id.data),form.pet.data,form.owner.data,form.pet_breed.data)
        DBConnection.close_db()
        return redirect(url_for('pet_records'))
    return render_template("pet_registration_form.html",form=form)

@app.route('/log_detail',methods = ['GET','POST'])
def log_details():
    data = Log.read_log()
    return render_template('disp_log.html',data=data)

@app.route('/pet_form',methods = ['GET','POST'])
def pet_form():
    DBConnection.connect_db()
    DBConnection.create_table()
    form = PetForm()
    if form.validate_on_submit():
        DBConnection.insert_data(form.pet.data,form.owner.data,form.pet_breed.data)
        DBConnection.close_db()
        return redirect(url_for('pet_records'))
    
    return render_template("pet_registration_form.html",form=form)
if __name__=='__main__':
    app.run()
