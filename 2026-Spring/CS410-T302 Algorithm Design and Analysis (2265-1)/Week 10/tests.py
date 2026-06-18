def test_ford_fulkerson():
    cases = [
        # Test 1: Simple flow network with two nodes and one edge
        ([
            [0, 1],
            [0, 0]
        ], 0, 1, 1),

        # Test 2: Flow network with multiple paths
        ([
            [0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]
        ], 0, 5, 23),

        # Test 3: Flow network with loops
        ([
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ], 0, 3, 2),

        # Test 4: Flow network with no feasible flow
        ([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ], 0, 2, 0),

        # Test 5: Flow network with multiple paths and a bottleneck
        ([
            [0, 10, 5, 0, 0],
            [0, 0, 15, 10, 0],
            [0, 0, 0, 5, 10],
            [0, 0, 0, 0, 15],
            [0, 0, 0, 0, 0]
        ], 0, 4, 15),

        # Test 6: Flow network with capacity zero edges
        ([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], 0, 3, 0),

        # Test 7: Flow network with large number of nodes
        ([
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], 0, 7, 2),

        # Test 8: Flow network with all edges having the same capacity
        ([
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ], 0, 3, 3),


        # Test 9: Flow network with a disconnected node
        ([
            [0, 1],
            [0, 0]
        ], 0, 1, 1),

        # Test 10: Flow network with a disconnected source and sink
        ([
            [0, 1],
            [0, 0]
        ], 0, 1, 1)

    ]
    return cases
