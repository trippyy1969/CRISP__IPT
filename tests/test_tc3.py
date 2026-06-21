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
    "101": ["A", "B", "C"]
}

companies = {

    "A": {
        "duration": 60,
        "rounds": 1,
        "panels": 1
    },

    "B": {
        "duration": 60,
        "rounds": 1,
        "panels": 1
    },

    "C": {
        "duration": 60,
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

if len(conflicts) > 0:
    print("TC3 PASS")
else:
    print("TC3 FAIL")