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

    # Create panel calendars
    for company, details in companies.items():

        panel_usage[company] = {}

        for panel in range(
            1,
            details["panels"] + 1
        ):

            panel_usage[company][panel] = []

    # Schedule interviews
    for student, company_list in students.items():

        previous_end = slot_start

        for company in company_list:

            duration = companies[company]["duration"]

            rounds = companies[company]["rounds"]

            for round_no in range(
                1,
                rounds + 1
            ):

                scheduled = False

                current_time = previous_end

                while (
                    current_time + duration
                    <= slot_end
                ):

                    start = current_time

                    end = (
                        current_time
                        + duration
                    )

                    for panel in range(
                        1,
                        companies[company]["panels"] + 1
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

                            previous_end = (
                                end
                                + break_time
                            )

                            scheduled = True

                            break

                    if scheduled:
                        break

                    current_time += 5

                if not scheduled:

                    conflicts.append(
                        {
                            "student": student,
                            "company": company,
                            "round": round_no,
                            "reason":
                            "No available slot"
                        }
                    )

                    break

    return schedule, conflicts