from src.utils import (format_departments)


def test_input_with_correct_shape_and_data():
    """Happiest path where the input is 'correct'.

    Input a list of dictionaries, with
    each dictionary containing a 'department' key.
    Expect a list of list, with the value of 'department'
    in each second-level list.
    """

    input = [
        {
            'staff_id': 1,
            'first_name': 'Duncan',
            'last_name': 'Crawley',
            'department': 'Beauty'
        },
        {
            'staff_id': 2,
            'first_name': 'Cat',
            'last_name': 'Hoang',
            'department': 'Footwear'
        }
    ]

    expected = [['Beauty'], ['Footwear']]

    assert format_departments(input) == expected


def test_input_not_mutated():
    """Enforces function purity.

    Expects input and output mem refs to be different.
    Expects input and expected values to be equal.
    """

    input = [
        {
            'staff_id': 1,
            'first_name': 'Duncan',
            'last_name': 'Crawley',
            'department': 'Beauty'
        },
        {
            'staff_id': 2,
            'first_name': 'Cat',
            'last_name': 'Hoang',
            'department': 'Footwear'
        }
    ]

    expected = [
        {
            'staff_id': 1,
            'first_name': 'Duncan',
            'last_name': 'Crawley',
            'department': 'Beauty'
        },
        {
            'staff_id': 2,
            'first_name': 'Cat',
            'last_name': 'Hoang',
            'department': 'Footwear'
        }
    ]

    output = format_departments(input)

    assert input is not output
    assert input == expected
