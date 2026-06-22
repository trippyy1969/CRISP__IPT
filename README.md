# Campus Recruitment Interview Scheduling Platform

## Overview

This project automates interview scheduling for campus recruitment drives.

The system schedules interviews for students shortlisted by different companies while ensuring:

* No student interview overlap
* Panel capacity constraints are respected
* Interview rounds occur sequentially
* Conflict detection for unschedulable interviews
* Fair scheduling using Round Robin
* Minimum 5-minute break between interviews

---

## Features

### Core Scheduling

* Automated interview scheduling
* Round Robin scheduling strategy
* Round precedence enforcement
* Panel capacity management
* Student availability tracking
* 5-minute break between interviews

### Conflict Detection

The system reports scheduling conflicts with detailed reasons:

* Panel capacity exhausted
* Student unavailable
* Insufficient remaining time

### Input Validation

The application validates:

* Positive interview duration
* Positive number of rounds
* Positive number of panels
* Valid student-company mappings
* Valid scheduling time window

### Web Application

* CSV upload interface
* Schedule dashboard
* Conflict dashboard
* Download schedule as CSV

---

## Project Structure

```text
IPT/
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── data/
│   ├── students.csv
│   ├── companies.csv
│   └── schedule.csv
│
├── tests/
│   └── test_scheduler.py
│
├── scheduler.py
├── input_data.py
├── validator.py
├── exporter.py
├── requirements.txt
├── docker_compose.yml
├── test_report.txt
└── README.md
```

---

## Input Files

### students.csv

```csv
student_id,companies
101,A;B
102,A
103,B
```

### companies.csv

```csv
company,duration,rounds,panels
A,30,2,2
B,45,1,1
```

---

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Flask application:

```bash
python app/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Docker Deployment

Build and start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:5000
```

Stop the application:

```bash
docker compose down
```


---

## Running Tests

```bash
python tests/test_scheduler.py
```

---

## Algorithm Used

### Round Robin Scheduling

Instead of completing all interviews for a single student first, the scheduler distributes interview opportunities fairly among students.

Benefits:

* Fairer scheduling
* Reduced waiting time concentration
* Better interview distribution
* Improved resource utilization

---

## Assumptions

* All interviews occur on a single day
* Time is represented internally in minutes
* Interview slots are continuous
* Students cannot attend overlapping interviews
* Company panels cannot exceed capacity
* Minimum 5-minute break between interviews

---

## Test Cases Implemented

* Basic Scheduling
* Panel Capacity Constraint
* Conflict Detection
* Round Precedence
* Fair Scheduling
* Break Enforcement
* Invalid Input Handling

---

## Output

The application generates:

* Interview Schedule Dashboard
* Conflict Dashboard
* Downloadable CSV Schedule

---

## Author

Tripti Gupta
IIT Bombay
