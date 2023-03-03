"""Contains utility functions that formats raw data for database insertion.

The incoming data will usually contain too much data 
to be inserted into a database in one go.
These utility functions will select smaller bits of data
and return them in a simpler data structure.
"""


def format_departments(staffs):
    """Get unique 'department' values from a List of staff Dicts.

    Get the 'department' values from a list of dicts representing each staff, 
    make them unique,
    and return them as one list of lists representing each unique department.

    Args:
        staffs:
            A list of dicts. Each dict is mapped to a staff row
            from the queried database.
            Each key of each dict is mapped to a staff column
            from the queried database.

    Returns:
        A list of departments.
        Each department is represented as a list of a string.
        Items of the top-level list are unique.
    """

    unique_departments = []

    for staff in staffs:
        department = [staff['department']]

        if department not in unique_departments:
            unique_departments.append(department)

    return unique_departments
