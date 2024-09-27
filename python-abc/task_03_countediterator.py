#!/usr/bin/python3

class CountedIterator:
    """
    A custom iterator that counts the number of items iterated over.

    This class wraps around an iterable and provides a method to
    retrieve the count of items iterated so far.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an
        iterable and sets the counter to zero.

        Args:
            iterable: Any iterable object
            (e.g., list, tuple, etc.) to be iterated over.
        """
        self.iter = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Returns the next item from the iterable and increments the count.

        Returns:
            The next item from the iterable.

        Raises:
            StopIteration: When there are no more items to iterate over.
        """
        try:
            item = next(self.iter)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the number of items that have been iterated over.

        Returns:
            int: The count of items iterated so far.
        """
        return self.count
