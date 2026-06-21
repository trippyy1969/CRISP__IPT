# main.py


from input_data import (
    get_students,
    get_companies,
    get_time_window,
    BREAK_TIME
)

from scheduler import (
    schedule_interviews
)

from exporter import (
    export_schedule,
    export_conflicts
)

def to_time(minutes):

    hour = minutes // 60

    minute = minutes % 60

    return (
        f"{hour:02d}:"
        f"{minute:02d}"
    )


students = get_students()

companies = get_companies()

slot_start, slot_end = (
    get_time_window()
)


schedule, conflicts = (
    schedule_interviews(
        students,
        companies,
        slot_start,
        slot_end,
        BREAK_TIME
    )
)

export_schedule(schedule)

export_conflicts(conflicts)

print("\n===== SCHEDULE =====\n")

for interview in schedule:

    print(

        f"Student {interview['student']} | "

        f"Company {interview['company']} | "

        f"Round {interview['round']} | "

        f"{to_time(interview['start'])}"

        f" - "

        f"{to_time(interview['end'])} | "

        f"Panel {interview['panel']}"
    )


print("\n===== CONFLICTS =====\n")

if len(conflicts) == 0:

    print("No conflicts found.")

else:

    for conflict in conflicts:

        print(

            f"Student {conflict['student']} | "

            f"Company {conflict['company']} | "

            f"Round {conflict['round']} | "

            f"{conflict['reason']}"
        )