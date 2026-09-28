import struct
import sys

EMPTY_LIST_BYTES = sys.getsizeof([])
SLOT_BYTES = struct.calcsize("P")


# def capacity_of(items: list) -> int:
def capacity_of(items) :
    """Slots CPython has reserved, read back out of the object's byte size."""
    return (sys.getsizeof(items) - EMPTY_LIST_BYTES) // SLOT_BYTES


grown: list[int] = []
previous = 0
print("len  capacity")
for value in range(1, 70):
    grown.append(value)
    if capacity_of(grown) != previous:
        previous = capacity_of(grown)
        print(f"{len(grown):>3}  {previous:>8}")