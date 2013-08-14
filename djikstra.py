def djikstra(graph, source):
    dist = {}
    previous = {}
    dist[source] = 0
    unsettled_nodes = graph.keys()
    settled_nodes = []
    while len(unsettled_nodes) > 0:
        nodes = [ (x, dist[x]) for x in unsettled_nodes if dist.has_key(x) ]
        nodes.sort(lambda x,y: cmp(x[1], y[1]))
        current = nodes[0]
        unsettled_nodes.remove(current[0])
        settled_nodes.append(current[0])
        dests = [ x for x in graph[current[0]].keys() if x not in settled_nodes ]
        for dest_node in dests:
            distance = graph[current[0]][dest_node]
            new_distance = dist[current[0]] + distance
            if not dist.has_key(dest_node) or dist[dest_node] > new_distance:
                dist[dest_node] = new_distance
                unsettled_nodes.append(dest_node)
    return dist



Graph = {'s':{'u':10, 'x':5},
         'u':{'v':1, 'x':2},
         'v':{'y':4},
         'x':{'u':3, 'v':9, 'y':2},
         'y':{'s':7, 'v':6}}

for node in Graph.keys():
    print "from {0}: {1}".format(node, djikstra(Graph, node))

