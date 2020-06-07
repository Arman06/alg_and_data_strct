from Queue import Queue
from MinHeap import Heap as PriorityQueue


class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted

    def add_edge(self, first, second, weight=1):
        self.graph[first, second] = weight
        if not self.directed:
            self.graph[second, first] = weight

    @property
    def nodes(self):
        return sorted(list(set([x for pair in self.graph.keys() for x in pair])))

    def neighbors(self, node):
        return sorted([pair[1] for pair in self.graph.keys() if pair[0] == node])

    def neighbors_with_weight(self, node):
        return sorted([(pair[1], self.graph[pair]) for pair in self.graph.keys() if pair[0] == node])

    def print(self):
        for node in self.nodes:
            print("Neighbors of " + node + ":", end=" ")
            for neighbor, weight in self.neighbors_with_weight(node):
                print(neighbor, "with weight %s" % str(weight), end="| ")
            print()

    def dfs(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
            for neighbour in self.neighbors(node):
                print(visited)
                self.dfs(neighbour, visited)

    def bfs(self, node):
        visited = [node]
        queue = Queue()
        queue.enqueue(node)
        while queue:
            node_ = queue.dequeue()
            for neighbor in self.neighbors(node_):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.append(neighbor)
            print(visited)

    def dijkstra(self, starting_node):
        unvisited = self.nodes
        nodes = [[node, float('inf'), node] for node in self.nodes]
        nodes[nodes.index([starting_node, float('inf'), starting_node])] = [starting_node, 0, starting_node]
        queue = PriorityQueue(nodes, key=lambda x: x[1])
        weight_index = 1
        current_node = queue.peek()
        short_paths = []
        while unvisited:
            unvisited.remove(current_node[0])
            short_paths.append(queue.delete())
            print(short_paths)
            for node, weight in self.neighbors_with_weight(current_node[0]):
                if node in unvisited:
                    new_weight = current_node[weight_index] + weight
                    if new_weight < queue.contents[queue.search(node, key=lambda x: x[0])][1]:
                        queue.delete(node, key=lambda x: x[0])
                        queue.insert([node, new_weight, current_node[0]])
            if queue:
                current_node = queue.peek()
            else:
                break
        return short_paths

    def prims(self, starting_node):
        unvisited = self.nodes
        nodes = [[node, float('inf'), node] for node in self.nodes]
        nodes[nodes.index([starting_node, float('inf'), starting_node])] = [starting_node, 0, starting_node]
        queue = PriorityQueue(nodes, key=lambda x: x[1])
        weight_index = 1
        current_node = queue.peek()
        min_spanning_tree = []
        while unvisited:
            unvisited.remove(current_node[0])
            min_spanning_tree.append(queue.delete())
            print(min_spanning_tree)
            for node, weight in self.neighbors_with_weight(current_node[0]):
                if node in unvisited:
                    new_weight = weight
                    if new_weight < queue.contents[queue.search(node, key=lambda x: x[0])][1]:
                        queue.delete(node, key=lambda x: x[0])
                        queue.insert([node, new_weight, current_node[0]])
            if queue:
                current_node = queue.peek()
            else:
                break
        return min_spanning_tree


graph = Graph(weighted=True)
graph.add_edge("A", "B", 6)
graph.add_edge("B", "C", 5)
graph.add_edge("C", "E", 5)
graph.add_edge("E", "D", 1)
graph.add_edge("D", "A", 1)
graph.add_edge("D", "B", 2)
graph.add_edge("B", "E", 2)
graph.add_edge("E", "K", 1)
graph.add_edge("E", "Z", 1)
graph.add_edge("K", "R", 1)
graph.add_edge("Z", "L", 1)


print(graph.graph)
print(graph.nodes)
print(graph.neighbors('B'))
graph.print()
graph.dfs("A")
graph.bfs("A")
print(graph.dijkstra("A"))
print(graph.prims("A"))