"""Contains utility functions that formats raw data for database insertion.

The incoming data will usually contain too much data 
to be inserted into a database in one go.
These utility functions will select smaller bits of data
and return them in a simpler data structure.
"""


import copy


def format_departments(staffs):
    return [[staff['department']] for staff in staffs]
