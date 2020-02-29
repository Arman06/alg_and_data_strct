class Graph:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, first, second, depth=0):
        if first in self.graph:
            self.graph[first].add(second)
        else:
            self.graph[first] = set(second)
        depth += 1
        if not self.directed:
            if depth == 1:
                self.add_edge(second, first, depth)
        else:
            if depth == 1:
                self.add_edge(second, None, depth)

    @property
    def nodes(self):
        return list(self.graph.keys())

    def neighbors(self, node):
        return list(self.graph[node])

    def print(self):
        for node in sorted(list(self.graph.keys())):
            print("Neighbors of " + node + ":", end=" ")
            for neighbor in sorted(list(self.graph[node])):
                print(neighbor, end=" ")
            print()

    def dfs(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
            for neighbour in sorted(list(self.graph[node])):
                print(visited)
                self.dfs(neighbour, visited)


graph = Graph(directed=False)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "G")
graph.add_edge("G", "B")
graph.add_edge("C", "B")
graph.add_edge("E", "K")
graph.add_edge("H", "I")
graph.add_edge("J", "K")
graph.add_edge("J", "H")
graph.add_edge("K", "C")
print(graph.graph)
print(graph.nodes)
print(graph.neighbors('A'))
graph.print()
graph.dfs("K")

