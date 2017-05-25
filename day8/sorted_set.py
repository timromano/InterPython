from bisect import bisect_left


class SortedSet:
    def __init__(self,items=None):
        """
        Return a sorted set
        :param items: sequence of values
        """
        #sorted(): returns a list, reguardless of which iterable is passed.
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return (index != len(self._items)) and self._items[index] == item

    def __len__(self):
        return (len(self._items))

    def __iter__(self):
        return iter(self._items)

