#!/usr/bin/python3

class VerboseList(list):
    """
    A subclass of the built-in list that provides
    verbose output for list operations.

    This class overrides several standard list
    methods (append, extend, remove, pop)
    to provide additional console output whenever
    these operations are performed.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a message.

        Args:
            item: The item to be added to the list.
        """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, extra):
        """
        Extends the list by appending elements from
        the iterable and prints a message.

        Args:
            extra: An iterable (e.g., list) whose
            items will be added to the list.
        """
        print("Extended the list with [{}] items.".format(len(extra)))
        super().extend(extra)

    def remove(self, delet):
        """
        Removes the first occurrence of the item
        from the list and prints a message.

        Args:
            delet: The item to be removed from the list.
        """
        print("Removed [{}] from the list.".format(delet))
        super().remove(delet)

    def pop(self, index=-1):
        """
        Removes and returns the item at the given position in the list.
        Prints a message with the popped item.

        Args:
            index (int): The index of the item to be
            removed and returned. Defaults to -1 (the last item).

        Returns:
            The item that was removed from the list.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
