# input_data.py

BREAK_TIME = 5


def get_students():

    return {
        "101": ["A", "B"],
        "102": ["A"],
        "103": ["B"]
    }


def get_companies():

    return {
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


def get_time_window():

    slot_start = 540   # 9:00 AM
    slot_end = 720     # 12:00 PM

    return slot_start, slot_end