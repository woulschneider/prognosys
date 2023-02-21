from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()



class Patient(db.Model):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone_number = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    street_address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class Diagnostics(db.Model):
    __tablename__ = 'diagnostics'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
