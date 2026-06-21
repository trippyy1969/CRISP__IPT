import csv

BREAK_TIME = 5


def get_students():

    students = {}

    with open(
        "students.csv",
        mode="r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            student_id = row["student_id"]

            companies = (
                row["companies"]
                .split(";")
            )

            students[
                student_id
            ] = companies

    return students


def get_companies():

    companies = {}

    with open(
        "companies.csv",
        mode="r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            companies[
                row["company"]
            ] = {

                "duration":
                int(
                    row["duration"]
                ),

                "rounds":
                int(
                    row["rounds"]
                ),

                "panels":
                int(
                    row["panels"]
                )
            }

    return companies


def get_time_window():

    return 540, 720