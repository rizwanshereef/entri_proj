
# REST API to schedule interviews based on available slots

## Installation

1. Environment Setup
~~~
python3 -m venv env
source env/bin/activate
~~~
2. Git Repo
~~~
git clone https://github.com/rizwanshereef/interview_scheduler.git
~~~
3. You can install the required dependencies using the command
~~~
pip install -r requirement.txt
~~~
4. Python server configuration
~~~
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver
~~~

## About Project

Interview scheduling is done via REST api endpoints implemented in Django python

### API List

* http://localhost:8000/candidates/
* http://localhost:8000/interviewer/
* http://localhost:8000/hr/

### API Endpoints Summary 

#### [./candidates/ ]

  ***Scope*** 

  Endpoint to candidate registration.

  ***API Parameters***

  * Candidate_id 
  * Name
  * Email_address
  * Phone
  * Start_Date
  * End_Date
  
 ***JSON Format*** 
 ~~~
{
    "candidate_id": null,
    "name": "",
    "email_address": "",
    "phone": null,
    "date": null,
    "start_time": null,
    "end_time": null
}
~~~
    
#### [./interviewer/ ]

***Scope***

API to register the interviewer available slots.

***API Parameters***

  * Interviewer_id
  * Name
  * Start_time
  * End_time

***JSON Format***
~~~
{
    "interviewer_id": null,
    "name": "",
    "date": null,
    "start_time": null,
    "end_time": null
}
~~~

#### [./hr/ ]

***Scope***

API to return scheduled interviews

***API Parameters***
  * Can_id  (Candidate Id)
  * Int_id  (Interviewer Id)

***JSON Format***

~~~
{
  "can_id": null,
  "int_id" : null
}
~~~

## Test Scenario

**Interview API**

URL: http://localhost:8000/candidates/

Input

~~~
    {
        "candidate_id": 1,
        "name": "Rizwan",
        "email_address": "rizwan@admin.com",
        "phone": 1234567,
        "date": "2020-05-28",
        "start_time": "10:44:00",
        "end_time": "22:44:00"
    }
~~~

Output:
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "candidate_id": 1,
        "name": "Rizwan",
        "email_address": "rizwan@admin.com",
        "phone": 1234567,
        "date": "2020-05-28",
        "start_time": "10:44:00",
        "end_time": "22:44:00"
    }
]
~~~

** Interviewer API **

URL:http://localhost:8000/interviewer/

Input:
~~~
    {
        "interviewer_id": 1,
        "name": "admin",
        "date": "2020-05-28",
        "start_time": "11:45:00",
        "end_time": "20:45:00"
    }
~~~

Output: 
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "interviewer_id": 1,
        "name": "admin",
        "date": "2020-05-28",
        "start_time": "11:45:00",
        "end_time": "20:45:00"
    }
]
~~~

**HR API**

URL:http://localhost:8000/hr/

Input:
~~~
{
  "can_id": 1,
  "int_id" : 2
}
~~~

Output:
~~~
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "message": "Slot Available",
    "date": "2020-05-28",
    "candidate ID": 1,
    "Candidate Name": "Rizwan",
    "Interviewer ID": 1,
    "Interviewer Name": "admin",
    "slot_start_time": "11:45:00",
    "slot_end_time": "20:45:00"
~~~
