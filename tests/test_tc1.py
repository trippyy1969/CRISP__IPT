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
    "102": ["B"]
}

companies = {
    "A": {
        "duration": 30,
        "rounds": 2,
        "panels": 2
    },

    "B": {
        "duration": 45,
        "rounds": 1,
        "panels": 1
    }
}

schedule, conflicts = schedule_interviews(
    students,
    companies,
    540,
    660,
    5
)

if len(conflicts) == 0:
    print("TC1 PASS")
else:
    print("TC1 FAIL")