import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Employer, Job, JobSeeker, JobApplication
from App.main import create_app
from App.controllers import ( create_user, get_all_users, create_job, view_jobs, apply_job, view_applicants, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 


# Command to create a new user (Employer or JobSeeker)
@user_cli.command("create")
@click.argument("id")
@click.argument("username", default="guest")
@click.argument("email", default="guest@mail.com")
@click.argument("phone", default="1234567")
@click.argument("person", default="jobseeker")  # Should be 'Employer' or 'JobSeeker'
def create_user_command(id, username, email, phone, person):
    create_user(id, username, email, phone, person)
    print(f'{username} created!')

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        get_all_users()

# Command to create a job (for employers)
@user_cli.command("create-job")
@click.argument("id")
@click.argument("title")
@click.argument("description")
@click.argument("salary", type=float)
@click.argument("employerid")
def create_job_command(id, title, description, salary, employerid):
    create_job(id, title, description, salary, employerid)
    print(f'{title} created!')

# Command to view all jobs
@user_cli.command("view-jobs")
def view_jobs_command():
    view_jobs()

# # Command for JobSeeker to apply to a job
@user_cli.command("apply-job")
@click.argument("id")
@click.argument("jobid")
@click.argument("jobseekerid")
def apply_job_command(id, jobid, jobseekerid):
    apply_job(id, jobid, jobseekerid)
        # , Status: {application.status}")

# Command for Employer to view job applicants for a specific job
@user_cli.command("view-applicants")
@click.argument("jobid")
def view_applicants_command(jobid):
    view_applicants(jobid)

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)