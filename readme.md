#CLI COMMANDS
```
CREATE USER
flask user create <id> <'username'> <'email'> <'phone'> <'employer'/'jobseeker'> #enter either 'jobseeker' or 'employer' as the last parameter

VIEW ALL USERS
flask user list

CREATE JOB
flask user create-job <id> <'title'> <'description'> <'salary'> <employerid>

VIEW JOBS
flask user view-jobs

APPLY JOB
flask user apply-job <applicationid> <job_id> <jobseeker_id>


VIEW APPLICANTS
flask user view-applicants <job_id>