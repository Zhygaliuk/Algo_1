class Graph:

    def __init__(self, vertexes):
        self.V = vertexes
        self.adj_list = {i: [] for i in range(1, vertexes + 1)}
        self.SCC_count = 0
        self.id = 0
        self.pre = [None] * (vertexes + 1)
        self.low = [None] * (vertexes + 1)
        self.stack = []
        self.visited = []

    def add_edge(self, from_vert, to_vert):
        self.adj_list[from_vert].append(to_vert)

    def find_SCCs(self):
        for vert in self.adj_list.keys():
            if vert not in self.visited:
                self.dfs(vert)
        return self.low

    def dfs(self, at):
        self.stack.append(at)
        self.visited.append(at)
        self.pre[at] = self.low[at] = self.id
        self.id += 1

        for to in self.adj_list[at]:
            if to not in self.visited:
                self.dfs(to)
            if to in self.stack:
                self.low[at] = min(self.low[at], self.low[to])

        if self.pre[at] == self.low[at]:
            self.SCC_count += 1

            while len(self.stack) > 0:
                peek = self.stack.pop()
                if peek == at:
                    break


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 2)
    graph.add_edge(4, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 4)

    print(graph.find_SCCs())
    print(graph.SCC_count)