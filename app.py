from flask import Flask, render_template, request, redirect, url_for
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.patients import Patient, Diagnostics, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nfummyjq:pO6jnSAUV3byLm0n6-IWdTkTiqS-DXRk@kesavan.db.elephantsql.com/nfummyjq'

migrate = Migrate(app, db)
#db = SQLAlchemy(app)
with app.app_context():
        db.init_app(app)

        db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        dob = request.form['dob']
        phone = request.form['phone']
        cpf = request.form['cpf']
        address = request.form['address']
        city = request.form['city']
        cep = request.form['cep']
        patient = Patient(first_name=first_name, last_name=last_name, gender=gender, date_of_birth=dob, phone_number=phone, cpf=cpf, street_address=address, city=city, cep=cep)
        db.session.add(patient)
        db.session.commit()
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/patient/<int:patient_id>', methods=['GET', 'POST'])
def patient(patient_id):
    if request.method == 'POST':
        if request.form.get('update'):
            patient = Patient.query.filter_by(id=patient_id).first()
            patient.first_name = request.form['first_name']
            patient.last_name = request.form['last_name']
            patient.address = request.form['address']
            patient.dob = request.form['dob']
            patient.phone = request.form['phone']
            patient.cpf = request.form['cpf']
            patient.city = request.form['city']
            patient.cep = request.form['cep']
            db.session.commit()
        elif request.form.get('delete'):
            patient = Patient.query.filter_by(id=patient_id).first()
            db.session.delete(patient)
            db.session.commit()
            return redirect(url_for('patients'))
    patient = Patient.query.filter_by(id=patient_id).first()
    return render_template('patient.html', patient=patient)


if __name__ == '__main__':
    app.run(debug=True)