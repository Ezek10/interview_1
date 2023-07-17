from collections import UserList


class MyList(UserList):
    def pop_with_default(self, index=-1, default=None):
        try:
            return super().pop(index)
        except IndexError:
            return default
