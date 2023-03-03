from src.utils import (format_departments, format_stock)
import pytest


@pytest.mark.skip
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


@pytest.mark.skip
def test_input_with_correct_shape_and_data():
    """The input has the key we want, nested within a list of dictionaries.

    The input is a list of dictionaries, with each dictionary 
    containing a 'department' key.
    Expects a list of lists, with only one item in each second-level list.
    That item is the value of 'department'
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


@pytest.mark.skip
def test_input_with_valid_desired_key__other_keys_and_shape_are_invalid():
    """The key we want is valid, but other data isn't.

    See test_input_with_correct_shape_and_data().
    Now the data we're not accessing is not the same as
    what's retrieved from the database.
    """

    input = [
        {
            'random_key': 'anything',
            'staff_id': 999,
            'department': 'Beauty'
        },
        {
            'wrong_shape': 2,
            'department': 'Footwear'
        }
    ]

    expected = [['Beauty'], ['Footwear']]

    assert format_departments(input) == expected


@pytest.mark.skip
def test_returned_values_are_unique():
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
        },
        {
            'staff_id': 3,
            'first_name': 'random',
            'last_name': 'person',
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
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }, {
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount_in_stock': 10
    }
]

    expected = [
    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }, {
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount_in_stock': 10
    }
]

    output = format_stock(input)

    assert input is not output
    assert input == expected


def test_input_with_correct_shape_and_data__1_item():
    """The input has the keys we want, nested within a list of dictionaries.

    The input is a list of dictionaries, with each dictionary 
    containing an 'item_name' and an 'amount_in_stock' key.
    Expects a list of lists, with two items in each second-level list.
    Those items are the values of 'item_name' and 'amount_in_stock'.
    """
    
    input = [
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        }
    ]

    expected = [['Louboutin Flip Flops', 5]]

    assert format_stock(input) == expected


def test_input_with_correct_shape_and_data__multiple_items():
    """See test_input_with_correct_shape_and_data__1_item().

    Now with >1 dicts in the list.
    """

    input = [
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        }, {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 10
        }
    ]

    expected = [['Louboutin Flip Flops', 5], ['Eau de Fromage', 10]]

    assert format_stock(input) == expected


def test_returned_values_are_unique():
    """
    Also test for other invalid keys and shape.
    See test_input_with_valid_desired_key__other_keys_and_shape_are_invalid().
    """

    input = [
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        }, {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 10
        }, {
            'item_name': 'test_name',
            'random property': ['Fragrance', 'Designer'],
            'amount_in_stock': 888
        }
    ]

    expected = [['Louboutin Flip Flops', 5], ['Eau de Fromage', 10], ['test_name', 888]]

    assert format_stock(input) == expected


def test_stock_with_same_name_will_add_amount_in_stock():
    """placeholder
    """

    input = [
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        }, {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 10
        }, {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 888
        }
    ]

    expected = [['Louboutin Flip Flops', 5], ['Eau de Fromage', 898]]

    assert format_stock(input) == expected
