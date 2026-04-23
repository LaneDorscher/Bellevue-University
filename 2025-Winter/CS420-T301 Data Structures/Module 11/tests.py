from module11_assignment import DynamicArray, DisjointSet, BloomFilter

def test_dynamic_array():
    dynamic_array = DynamicArray()

    # Adding items
    dynamic_array.add(1)
    dynamic_array.add(2)
    dynamic_array.add(3)
    dynamic_array.add(4)
    dynamic_array.add(5)

    # Test cases
    tests = [
        (dynamic_array.get(0), 1, "Get first element"),  # Test 1
        (dynamic_array.get(2), 3, "Get third element"),  # Test 2
        (dynamic_array.count, 5, "Count after adding items"),  # Test 3
    ]

    # Testing dynamic resizing
    dynamic_array.add(6)
    tests.append((dynamic_array.count, 6, "Count after resizing"))  # Test 4

    # Test removing an item
    dynamic_array.remove(1)  # Removes '2'
    tests.append((dynamic_array.get(1), 3, "Get element after removal"))  # Test 5
    tests.append((dynamic_array.count, 5, "Count after removal"))  # Test 6

    # Test out of bounds
    try:
        dynamic_array.get(10)
        tests.append((False, True, "Accessing out of bounds (should fail)"))  # Test 7
    except IndexError:
        tests.append((True, True, "Accessing out of bounds (should fail)"))  # Test 7

    # Test removing from an empty index
    try:
        dynamic_array.remove(10)
        tests.append((False, True, "Removing from out of bounds (should fail)"))  # Test 8
    except IndexError:
        tests.append((True, True, "Removing from out of bounds (should fail)"))  # Test 8

    # Testing underflow resize
    dynamic_array.remove(4)  # Current count is 4, capacity should resize
    dynamic_array.remove(3)
    dynamic_array.remove(2)
    dynamic_array.remove(1)  # Current count is 1, capacity should resize
    tests.append((dynamic_array.count, 1, "Count after multiple removals"))  # Test 9

    # Test adding after removals
    dynamic_array.add(7)
    tests.append((dynamic_array.get(1), 7, "Get new element after re-adding"))  # Test 10

    return tests


def test_disjoint_set():
    ds = DisjointSet(10)
    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(5, 6)
    ds.union(7, 8)

    return [
        (ds.find(1) == ds.find(3), True, "Check if 1 and 3 are connected"),  # Test 1
        (ds.find(1) == ds.find(4), False, "Check if 1 and 4 are not connected"),  # Test 2
        (ds.find(4) == ds.find(6), True, "Check if 4 and 6 are connected"),  # Test 3
        (ds.find(7) == ds.find(8), True, "Check if 7 and 8 are connected"),  # Test 4
        (ds.find(3) == ds.find(7), False, "Check if 3 and 7 are not connected"),  # Test 5
    ]


def test_bloom_filter():
    bf = BloomFilter(1000)
    bf.add("test_item")
    bf.add("hello")
    bf.add("world")

    return [
        (bf.check("test_item"), True, "Check if 'test_item' is present"),  # Test 6
        (bf.check("nonexistent_item"), False, "Check if 'nonexistent_item' is not present"),  # Test 7
        (bf.check("hello"), True, "Check if 'hello' is present"),  # Test 8
        (bf.check("world"), True, "Check if 'world' is present"),  # Test 9
        (bf.check("another"), False, "Check if 'another' is not present"),  # Test 10
    ]
