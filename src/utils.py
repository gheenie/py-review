"""Contains utility functions that formats raw data for database insertion.

The incoming data will usually contain too much data 
to be inserted into a database in one go.
These utility functions will select smaller bits of data
and return them in a simpler data structure.
"""


def format_departments(staffs):
    unique_departments = []

    for staff in staffs:
        department = [staff['department']]

        if department not in unique_departments:
            unique_departments.append(department)

    return unique_departments
