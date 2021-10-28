"""Common exceptions"""


class InventoryException(Exception):
    """Base exception class for Inventory exceptions"""
    pass


class UnequippableItem(InventoryException):
    """Raised when attempting to equip an item that cannot be equipped"""

    def __init__(self, item):
        self.item = item
        self.message = f"Cannot equip {item} because it is not equippable."
        super().__init__(self.message)
