#!/usr/bin/env python3
"""Module defining VerboseList which extends Python's built-in list."""


class VerboseList(list):
    """A list subclass that prints notifications when items are modified."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list by appending elements from iterable and print notification."""
        # Convert to list to preserve length if generator is passed
        items = list(iterable)
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove first occurrence of item and print notification before removing."""
        # Print message only if item exists in list
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)  # Raises ValueError automatically if item not in list

    def pop(self, index=-1):
        """Remove and return item at index (default last) with a notification."""
        item = self[index]  # Access item first; raises IndexError if list is empty
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


if __name__ == "__main__":
    # --- Testing ---
    v = VerboseList()

    # 1. Test append
    v.append(10)
    v.append(20)

    # 2. Test extend
    v.extend([30, 40, 50])

    # 3. Test pop (default index -1)
    popped_item = v.pop()

    # Test pop with specific index
    popped_item_first = v.pop(0)

    # 4. Test remove
    v.remove(30)

    print(f"\nFinal List State: {v}")