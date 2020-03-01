from Queue import Queue


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

    def print(self):
        for node in self.nodes:
            print("Neighbors of " + node + ":", end=" ")
            for neighbor in self.neighbors(node):
                print(neighbor, "", end=" ")
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

    def dijkstra(self, node):
      pass


graph = Graph(directed=True)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("E", "F")
graph.add_edge("C", "F")

print(graph.graph)
print(graph.nodes)
print(graph.neighbors('B'))
graph.print()
graph.dfs("A")
graph.bfs("A")