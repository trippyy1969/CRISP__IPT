import csv


def to_time(minutes):

    hour = minutes // 60
    minute = minutes % 60

    return f"{hour:02d}:{minute:02d}"


def export_schedule(schedule):

    with open(
        data/schedule.csv,
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "student",
            "company",
            "round",
            "start",
            "end",
            "panel"
        ])

        # Schedule rows
        for interview in schedule:

            writer.writerow([

                interview["student"],

                interview["company"],

                interview["round"],

                to_time(
                    interview["start"]
                ),

                to_time(
                    interview["end"]
                ),

                interview["panel"]

            ])


def export_conflicts(conflicts):

    with open(
        "conflicts.csv",
        mode="w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "student",
            "company",
            "round",
            "reason"
        ])

        # Conflict rows
        for conflict in conflicts:

            writer.writerow([

                conflict["student"],

                conflict["company"],

                conflict["round"],

                conflict["reason"]

            ])