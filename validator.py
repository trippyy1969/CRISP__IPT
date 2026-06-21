def validate_companies(companies):

    for company, details in companies.items():

        if details["duration"] <= 0:

            raise ValueError(
                f"{company}: Duration must be positive"
            )

        if details["rounds"] <= 0:

            raise ValueError(
                f"{company}: Rounds must be positive"
            )

        if details["panels"] <= 0:

            raise ValueError(
                f"{company}: Panels must be positive"
            )


def validate_students(
    students,
    companies
):

    for student, company_list in students.items():

        if not student.strip():

            raise ValueError(
                "Student ID cannot be empty"
            )

        for company in company_list:

            if company not in companies:

                raise ValueError(
                    f"{company} does not exist in companies.csv"
                )


def validate_time_window(
    slot_start,
    slot_end
):

    if slot_start >= slot_end:

        raise ValueError(
            "Slot start must be before slot end"
        )


def validate_all(
    students,
    companies,
    slot_start,
    slot_end
):

    validate_companies(
        companies
    )

    validate_students(
        students,
        companies
    )

    validate_time_window(
        slot_start,
        slot_end
    )