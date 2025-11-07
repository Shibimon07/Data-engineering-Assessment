from service.database import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    address_line1 = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    pincode = db.Column(db.String(10))

    employment = db.relationship('EmploymentInfo', backref='user', cascade='all, delete-orphan')
    bank = db.relationship('UserBankInfo', backref='user', cascade='all, delete-orphan')


class EmploymentInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    company_name = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_current = db.Column(db.Boolean)


class UserBankInfo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bank_name = db.Column(db.String(100))
    account_number = db.Column(db.String(50))
    ifsc = db.Column(db.String(20))
    account_type = db.Column(db.String(50))
