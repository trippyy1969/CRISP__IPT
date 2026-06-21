# scheduler.py


def overlap(start1, end1, start2, end2):

    return start1 < end2 and end1 > start2


def student_free(
    student,
    start,
    end,
    schedule,
    break_time
):

    for interview in schedule:

        if interview["student"] == student:

            buffered_start = (
                interview["start"] - break_time
            )

            buffered_end = (
                interview["end"] + break_time
            )

            if overlap(
                start,
                end,
                buffered_start,
                buffered_end
            ):
                return False

    return True


def panel_free(
    company,
    panel,
    start,
    end,
    panel_usage
):

    interviews = panel_usage[company][panel]

    for interview in interviews:

        if overlap(
            start,
            end,
            interview["start"],
            interview["end"]
        ):
            return False

    return True


def schedule_interviews(
    students,
    companies,
    slot_start,
    slot_end,
    break_time
):

    schedule = []
    conflicts = []

    panel_usage = {}

    for company, details in companies.items():

        panel_usage[company] = {}

        for panel in range(
            1,
            details["panels"] + 1
        ):
            panel_usage[company][panel] = []

    # --------------------------
    # Student availability
    # --------------------------

    student_next_available = {}

    for student in students:
        student_next_available[student] = slot_start

    # --------------------------
    # Create initial queue
    # ONLY ROUND 1
    # --------------------------

    pending = []

    for student, company_list in students.items():

        for company in company_list:

            pending.append({

                "student": student,
                "company": company,
                "round": 1

            })

    # --------------------------
    # Main loop
    # --------------------------

    while pending:

        pending.sort(
            key=lambda x:
            student_next_available[
                x["student"]
            ]
        )

        task = pending.pop(0)

        student = task["student"]
        company = task["company"]
        round_no = task["round"]

        duration = companies[
            company
        ]["duration"]

        current_time = (
            student_next_available[
                student
            ]
        )

        scheduled = False

        while (
            current_time + duration
            <= slot_end
        ):

            start = current_time
            end = current_time + duration

            for panel in range(

                1,

                companies[
                    company
                ]["panels"] + 1
            ):

                if (

                    student_free(
                        student,
                        start,
                        end,
                        schedule,
                        break_time
                    )

                    and

                    panel_free(
                        company,
                        panel,
                        start,
                        end,
                        panel_usage
                    )

                ):

                    interview = {

                        "student": student,

                        "company": company,

                        "round": round_no,

                        "start": start,

                        "end": end,

                        "panel": panel
                    }

                    schedule.append(
                        interview
                    )

                    panel_usage[
                        company
                    ][panel].append(
                        interview
                    )

                    student_next_available[
                        student
                    ] = (
                        end
                        + break_time
                    )

                    scheduled = True

                    # ------------------
                    # Unlock next round
                    # ------------------

                    total_rounds = (
                        companies[
                            company
                        ]["rounds"]
                    )

                    if round_no < total_rounds:

                        pending.append({

                            "student": student,

                            "company": company,

                            "round": round_no + 1

                        })

                    break

            if scheduled:
                break

            current_time += 5

        if not scheduled:

            conflicts.append({

                "student": student,

                "company": company,

                "round": round_no,

                "reason":
                "No available slot"

            })

    return schedule, conflicts