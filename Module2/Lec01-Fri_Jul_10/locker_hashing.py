# locker_hashing.py

def locker_hash(student_name, number_of_rows):
    """
    Convert a student name into a locker row number.

    Example:
    locker_hash("Mia", 5) should return a number from 0 to 4.
    """
    # TODO: Start with a total of 0

    # TODO: Loop through each character in student_name

    # TODO: Convert each character to a number using ord()

    # TODO: Add that number to the total

    # TODO: Use modulo to keep the result inside the number of rows

    # TODO: Return the row number
    pass


def assign_students(student_names, number_of_rows):
    """
    Print each student name and the locker row assigned by locker_hash.
    """
    # TODO: Loop through the list of names

    # TODO: Print each name with its assigned locker row
    pass


# Demo data
students = [
    "Ava",
    "Liam",
    "Noah",
    "Mia",
    "Zoe",
]

assign_students(students, 5)
