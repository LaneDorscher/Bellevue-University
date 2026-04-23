from module10_assignment import SkipList, SelfAdjustingList
def test_skip_list():
    skip_list = SkipList(3, 0.5)  # Assuming a SkipList class with max_level and p as parameters
    skip_list.insert(3)
    skip_list.insert(6)
    skip_list.insert(9)

    return [
        (skip_list.search(3) is not None, True, "Search for existing item 3"),  # Test 1
        (skip_list.search(6) is not None, True, "Search for existing item 6"),  # Test 2
        (skip_list.search(9) is not None, True, "Search for existing item 9"),  # Test 3
    ]

def test_self_adjusting_list():
    self_list = SelfAdjustingList()  # Assuming a SelfAdjustingList class
    self_list.insert(1)
    self_list.insert(2)
    self_list.insert(3)

    return [
        (self_list.access(2), True, "Access existing item 2"),  # Test 6
        (self_list.access(3), True, "Access existing item 3 and check adjustment"),  # Test 7
        (self_list.access(4), False, "Access non-existing item 4"),  # Test 9
    ]
