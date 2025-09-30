"""Functions to keep track and alter inventory."""

UNKNOWN_KEY = 'unknown key'
def create_inventory(items: list):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = dict()
    
    for key in items:
        existing_key = inventory.get(key, UNKNOWN_KEY)
        if existing_key != UNKNOWN_KEY:
            inventory[key] = inventory[key] + 1
        else:
            inventory[key] = 1

    return inventory
        


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        existing_key = inventory.get(item, UNKNOWN_KEY)
        if existing_key != UNKNOWN_KEY:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        existing_key = inventory.get(item, UNKNOWN_KEY)
        if existing_key != UNKNOWN_KEY and existing_key != 0:
            inventory[item] = inventory[item] - 1

    return inventory
            


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    existing_key = inventory.get(item, UNKNOWN_KEY)
    if existing_key != UNKNOWN_KEY:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inventory_list = []

    for key, value in inventory.items():
        if value > 0:
            item = (key, value)
            inventory_list.append(item)

    return inventory_list

