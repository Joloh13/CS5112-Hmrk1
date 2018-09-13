# Please see instructions.txt for the description of this problem.
import heapq
import copy

def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    #
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.txt for additional information about the
    # return value of this method.

    discovered = []
    hq = []
    distances = {source: 0}
    heapq.heappush(hq, [0, source, [source]])

    while hq:

        lowestCost = heapq.heappop(hq) #will return [weight, node]

        if lowestCost[1] == target:
            print("This is the distance of the shortest path:{}".format(distances[lowestCost[1]]))
            print("This is the shortest path:{}".format(lowestCost[2]))
            return lowestCost[2], distances[lowestCost[1]]

        if lowestCost[1] not in discovered:
            discovered.append(lowestCost[1])
            for x in graph.get_neighbors(lowestCost[1]):
                tentativeDist = distances[lowestCost[1]] + x[1]
                if x[0] in distances:
                    if tentativeDist < distances[x[0]]:
                        distances[x[0]] = tentativeDist
                else:
                    distances[x[0]] = tentativeDist

                tentativeList = copy.copy(lowestCost[2])
                tentativeList.append(x[0])
                heapq.heappush(hq, (x[1], x[0], tentativeList))





















