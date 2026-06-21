import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from scheduler import schedule_interviews

students = {
    "101": ["A"],
    "102": ["A"],
    "103": ["A"]
}

companies = {
    "A": {
        "duration": 30,
        "rounds": 1,
        "panels": 2
    }
}

schedule, conflicts = schedule_interviews(
    students,
    companies,
    540,
    600,
    5
)

if len(schedule) == 3:
    print("TC2 PASS")
else:
    print("TC2 FAIL")