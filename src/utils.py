"""Contains utility functions that formats raw data for database insertion.

The incoming data will usually contain too much data 
to be inserted into a database in one go.
These utility functions will select smaller bits of data
and return them in a simpler data structure.
"""


def format_departments(staffs):
    """Transforms a list of staff dicts into a list of unique [department].

    Gets the 'department' values from a list of dicts representing each staff.
    Puts each department in a single-item list.
    Removes duplicates and returns them as 
    one list of lists representing each unique department.

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

    formatted_departments = []

    for staff in staffs:
        department = [staff['department']]

        if department not in formatted_departments:
            formatted_departments.append(department)

    return formatted_departments


def format_stock(stock):
    """Transforms a list of item dicts into a list of [unique item_name, total amount_in_stock].

    Gets the 'item_name' and 'amount_in_stock' values from a list of dicts representing each item.
    Puts each item name and stock amount in a list.
    In cases of duplicate item names, keep item names unique and add to the amount_in_stock instead.
    Return them as one list of lists representing each unique item.

    Args:
        stock:
            A list of dicts. Each dict is mapped to an item row
            from the queried database.
            Each key of each dict is mapped to an item column
            from the queried database.

    Returns:
        A list of items.
        Each item is represented as a list of item_name: str and amount_in_stock: int.
        Item names are unique.
    """

    formatted_stock = []
    # Key will be an item name, value will be a ref to the corresponding element in unique_stock.
    existing_items = {}

    for item in stock:
        item_name = item['item_name']
        amount_in_stock = item['amount_in_stock']

        if item_name not in existing_items:
            formatted_item = [item_name, amount_in_stock]

            formatted_stock.append(formatted_item)

            existing_items[item_name] = formatted_item
        else:
            existing_items[item_name][1] += amount_in_stock
    
    return formatted_stock


def format_features(stock):
    """placeholder
    """
    
    formatted_features = []

    for item in stock:
        for feature in item['features']:
            formatted_feature = [feature]

            if formatted_feature not in formatted_features:
                formatted_features.append(formatted_feature)

    return formatted_features
