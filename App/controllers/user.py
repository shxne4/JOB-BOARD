from App.models import User, Employer, Job, JobSeeker, JobApplication
from App.database import db


def create_user(id, username, email, phone, person):
    if person.lower() not in ['employer', 'jobseeker']:
        return None, "Error: only 'employer' or 'jobseeker' allowed"

    if person.lower() == 'employer':
        user = Employer(id=id, username=username, email=email, phone=phone, person=person)
    else:
        user = JobSeeker(id=id, username=username, email=email, phone=phone, person=person)

    db.session.add(user)
    db.session.commit()
    return user

    def __repr__(self):
        return f'<User {self.id }{self.username} {self.email} {self.phone} {self.person}>'

def get_all_users():
     users = User.query.all()
     for guy in users:
        print ('User ID: ', guy.id, ' Username: ', guy.username, ' Email: ', guy.email, ' Phone: ', guy.phone, ' User Type: ', guy.person )


def create_job(id, title, description, salary, employerid):
   
    job = Job(id=id, title=title, description=description, salary=salary, employerid=employerid)
    db.session.add(job)
    db.session.commit()
    return job, "Job added successfully"

def view_jobs():
    jobs = Job.query.all()
    if jobs:
        for job in jobs:
            print('Job ID: ', job.id, ' Title: ', job.title, ' Description: ', job.description, ' Salary: ', job.salary, ' Employer ID: ', job.employerid )
    else:
        return "No jobs listed"

def apply_job(id, jobid, jobseekerid):
    jobs = Job.query.all()
    jobseekers = JobSeeker.query.all()

    if not jobs:
        return f"Job {jobid} does not exist"
    if not jobseekers:
        return f"Jobseeker {jobseekerid} does not exist"

    application = JobApplication(id=id, jobid=jobid, jobseekerid=jobseekerid)
    db.session.add(application)
    db.session.commit()
    return application, f"Jobseeker {jobseekerid} applied to Job {jobid} successfully"

def view_applicants(jobid):

    applicants = JobApplication.query.filter_by(jobid=jobid).all()
    if applicants:
        for applicant in applicants:
            print (applicant.jobseekerid )
    else:
        return "No applicants available"
    