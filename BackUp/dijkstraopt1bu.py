# Sample Solution: Map Routing

# Graphs whose vertices are points in the plane and,
# are connected by edges whose weights are Euclidean distances.
# ==============================================================================

from numpy import Inf
import math

def euclidean_distance(n1, n2):
    d = math.sqrt( (n2[1]-n1[1])**2 + (n2[0]-n1[0])**2 )
    return  round(d, 1)
# =========================================
nodes = [ ]
cons = [ ]
# filename = 'USACase\Map.txt'
filename = 'SampleCase\Map.txt'
fhand = open(filename)
lines = []
for line in fhand:
    if line.strip():
        line = [int(i) for i in line.split()]
        lines.append(line)
fhand.close()

v, e =  lines[0]
# print(v, e)
for i in range(1, v+1):
    nodeinfo = lines[i]
    nodes.append((nodeinfo[1], nodeinfo[2]))
# print(nodes)
for i  in  range(v+1, (v+1)+e):
    coninfo = lines[i]
    cons.append((coninfo[0], coninfo[1]))
# print(cons)

graph = {}
for i in range(v):
    graph[i] = []

for c in cons:
    A = c[0]
    B = c[1]
    weigth = euclidean_distance(nodes[A], nodes[B])
    RouteAB = (B, weigth)
    RouteBA = (A, weigth)
    graph[A].append(RouteAB)
    graph[B].append(RouteBA)
print(graph)
# =======================================


# ========================
import heapq
def  re_init_dist(dist, n):
    i = 0
    while dist[i] != Inf :
        dist[i] = Inf
        i += 1
        if i >= n :
            break
    return dist
def  clear_visited(visited, n):
    i = 0
    while visited[i] != False :

        visited[i] = False
        i += 1
        if i >= n :
            break
    return visited

def  lazy_dijkstras (graph,  root,  distances, visitedVs, n):
    dist      = re_init_dist(distances, n)
    visited = clear_visited(visitedVs, n)
    dist[root] = 0
    # set up priority queue
    pq = [(0, root)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = round(dist[u] + l, 1)
                heapq.heappush(pq, (dist[v], v))
    return dist




# output = lazy_dijkstras(graph, 0, dist, visited, n)
# print(output)
# ================================
# filename = 'SampleCase\Routes.txt'
filename = 'USACase\ShortRoutes100.txt'
fhand_routes = open(filename)
routes_lines = []
for line in fhand_routes:
    if line.strip():
        line = [int(i) for i in line.split()]
        routes_lines.append(line)
fhand_routes.close()
# print(routes_lines)

#================================
# output_filename = 'Output\samplecaseOut.txt'
output_filename = 'Output/usacaseOut.txt'
outputFileHandler = open(output_filename, 'w')

queries = routes_lines[1:]

n     = len(graph)
dist = [Inf]*n
visited = [False]*n

for query in queries:
    start = query[0]
    end = query[1]
    dijkstra_output =lazy_dijkstras(graph, start, dist, visited, n)
    # print(dijkstra_output)
    # print(dijkstra_output[end])
    outputFileHandler.write(str(dijkstra_output[end]))
    outputFileHandler.write('\n')

outputFileHandler.close()

# ==
