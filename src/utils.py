from collections import UserList


class MyList(UserList):
    """list class with an implementation for a pop method with default
    """
    def pop_with_default(self, index=-1, default=None):
        """remove and returns the item in index from the list, in case
        there's no item in the list returns default

        Args:
            index (int, optional): item index to remove. Defaults to -1.
            default (_type_, optional): default value to return. Defaults to None.
        """
        try:
            return super().pop(index)
        except IndexError:
            return default
