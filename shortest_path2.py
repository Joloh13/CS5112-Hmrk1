try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
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

  # YOUR CODE HERE
  discovered =[]
  q = Q.PriorityQueue()
  q.put((0, source, [source]))
  while not q.empty():
      lowestCost = q.get()
      if lowestCost[1] == target:
          return (lowestCost[2], lowestCost[0])
      if lowestCost[1] not in discovered:
          discovered.append(lowestCost[1])
          for i,x in enumerate(graph.get_neighbors(lowestCost[1])):
              copyList = copy.copy(lowestCost[2])
              copyList.append(x[0])
              q.put((x[1]+lowestCost[0], x[0], copyList))
