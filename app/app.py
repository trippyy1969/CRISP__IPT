import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

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
    export_schedule
)

app = Flask(__name__)

def to_time(minutes):

    hour = minutes // 60

    minute = minutes % 60

    return f"{hour:02d}:{minute:02d}"

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/generate",
    methods=["POST"]
)
def generate():

    students_file = request.files[
        "students_file"
    ]

    companies_file = request.files[
        "companies_file"
    ]

    students_file.save(
        "data/students.csv"
    )

    companies_file.save(
        "data/companies.csv"
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

    for interview in schedule:

        interview["start_time"] = (
            to_time(
                interview["start"]
            )
        )

        interview["end_time"] = (
            to_time(
                interview["end"]
            )
        )

    export_schedule(
    schedule
    )

    return render_template(
        "result.html",
        schedule=schedule,
        conflicts=conflicts
    )

@app.route("/download")
def download():

    return send_file(
        "data/schedule.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)