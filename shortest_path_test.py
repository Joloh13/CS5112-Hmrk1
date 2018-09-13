# This is a short test file, given to you to ensure that our grading scripts can grade your file.
# Please do not modify it.
# You should only submit "graph_adjacency_list.py", "graph_edge_list.py", and "shortest_path.py".

# This tests the simplest case: adding a single edge to the graph and checking the shortest path from one node to the other.

from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph
from shortest_path import shortest_path
import sys
import traceback

# try:
#   print("Testing with adjacency list graph...")
#   adjacency_graph = AdjacencyGraph()
#   adjacency_graph.add_edge('1', '3', 2)
#   adjacency_graph.add_edge('1', '4', 16)
#   adjacency_graph.add_edge('1', '2', 6)
#   adjacency_graph.add_edge('2', '5', 4)
#   adjacency_graph.add_edge('2', '4', 5)
#   adjacency_graph.add_edge('3', '2', 7)
#   adjacency_graph.add_edge('3', '5', 3)
#   adjacency_graph.add_edge('3', '6', 8)
#   adjacency_graph.add_edge('4', '7', 3)
#   adjacency_graph.add_edge('1', '7', 14)
#   adjacency_graph.add_edge('5', '4', 4)
#   adjacency_graph.add_edge('5', '7', 10)
#   adjacency_graph.add_edge('6', '7', 1)
#   print(shortest_path(adjacency_graph, '1', '7'))
#   if shortest_path(adjacency_graph, 'a', 'b') != (['a','b'], 1):
#     print "Your code ran, but did NOT output the shortest distance from 'a' to 'b' when your adjacency list graph had the edge ('a', 'b', 1) added."
#   else:
#     print "Your code ran, and it correctly output the shortest distance from 'a' to 'b' when your adjacency list graph had the edge ('a', 'b', 1) added."
# except:
#   print "Your code produced this error when adding edge ('a', 'b', 1) to the adjacency list graph or getting the shortest path from 'a' to 'b'."
#   print sys.exc_info()[0]

try:
  print("Testing with edge list graph...")
  edge_graph = EdgeGraph()
  edge_graph.add_edge('s', 'a', 3)
  edge_graph.add_edge('s', 'b', 4)
  edge_graph.add_edge('a', 'c', 2)
  edge_graph.add_edge('a', 'f', 7)
  edge_graph.add_edge('a', 'b', 6)
  edge_graph.add_edge('b', 'f', 5)
  edge_graph.add_edge('c', 'f', 1)
  edge_graph.add_edge('c', 't', 8)
  edge_graph.add_edge('f', 't', 4)
  print(shortest_path(edge_graph, 's', 't'))
  if shortest_path(edge_graph, 's', 't') != (['a', 'b', 'c', 'd'], 11):
    print "Your code ran, but did NOT output the shortest distance from 'a' to 'b' when your edge list graph had the edge ('a', 'b', 1) added."
  else:
    print "Your code ran, and it correctly output the shortest distance from 'a' to 'b' when your edge list graph had the edge ('a', 'b', 1) added."
except AttributeError:
  print "Your code produced this error when adding edge ('a', 'b', 1) to the edge list graph or getting the shortest path from 'a' to 'b'."
  print sys.exc_info()[0]
  traceback.print_exc()
