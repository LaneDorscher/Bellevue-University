# Author:   Lane Dorscher
# Date:     05/20/2026

#renamed arguments for clarity sake from psuedo code
def ford_fulkerson(graph, source, sink):
    """
    Implement the Ford-Fulkerson algorithm to compute the maximum flow in the network 'graph' from 
    source 's' to sink 't'. Return the value of the maximum flow.
    """
    flow = 0
    parent = [-1] * len(graph)

    while (bfs(graph, source, sink, parent)):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        flow += path_flow
    return flow

def bfs(graph, source, sink, parent):

    visited = [False] * len(graph)
    queue = []  #queue collections.deque for faster queue handling
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)

        for i, val in enumerate(graph[u]):
            if visited[i] is False and val > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u
    return visited[sink]




