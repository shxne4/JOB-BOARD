from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(25))
    email = db.Column(db.String(40))
    phone = db.Column(db.String(7))
    person = db.Column(db.String(10))

    def __init__(self, id, username, email, phone, person):
        self.id=id
        self.username=username
        self.email=email
        self.phone=phone
        self.person=person

class Employer(User):
    jobs = db.relationship('Job', backref='user', lazy=True)
    applications = db.relationship('JobApplication', backref='user', lazy=True)

    def __init__(self, id, username, email, phone, person):
        self.id=id
        self.username=username
        self.email=email
        self.phone=phone
        self.person=person

class JobSeeker(User):
    applications = db.relationship('JobApplication', backref='jobseeker', lazy=True)

    def __init__(self, id, username, email, phone, person):
        self.id=id
        self.username=username
        self.email=email
        self.phone=phone
        self.person=person


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    employerid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    applications = db.relationship('JobApplication', backref='job', lazy=True)

    def __init__(self,id, title, description, salary, employerid):
        self.id=id
        self.title=title
        self.description=description
        self.salary=salary
        self.employerid=employerid

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # status =  db.Column(db.String, nullable=False, default='Pending')
    jobid = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    jobseekerid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __init__(self, id, jobid, jobseekerid):
        self.id=id
        self.jobid=jobid
        self.jobseekerid=jobseekerid
        
        
