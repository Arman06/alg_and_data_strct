import Queue


class Graph:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, first, second, depth=0):
        if first in self.graph and second not in self.graph[first] and second is not None:
            self.graph[first].append(second)
        elif first not in self.graph:
            self.graph[first] = [second] if second is not None else []
        depth += 1
        if not self.directed:
            if depth == 1:
                self.add_edge(second, first, depth)
        else:
            if depth == 1:
                self.add_edge(second, None, depth)

    @property
    def nodes(self):
        return sorted(list(self.graph.keys()))

    def neighbors(self, node):
        return sorted(self.graph[node])

    def print(self):
        for node in self.nodes:
            print("Neighbors of " + node + ":", end=" ")
            for neighbor in self.neighbors(node):
                print(neighbor, end=" ")
            print()

    def dfs(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
            for neighbour in self.neighbors(node):
                print(visited)
                self.dfs(neighbour, visited)

    def bfs(self, node):
        visited = [node]
        queue = Queue.Queue()
        queue.enqueue(node)
        while queue:
            node_ = queue.dequeue()
            for neighbor in self.neighbors(node_):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.append(neighbor)
            print(visited)

    # @property
    # def adj_matrix(self):
    #


graph = Graph(directed=True)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("E", "F")
graph.add_edge("C", "F")

print(graph.graph)
print(graph.nodes)
print(graph.neighbors('A'))
graph.print()
graph.dfs("A")
graph.bfs("A")



