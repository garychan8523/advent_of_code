import networkx as nx
import math


class Solution():
    def part1(self, data):
        g = nx.Graph()
        for line in data:
            name, cmps = line.split(": ")
            for cmp in cmps.split():
                g.add_edge(name, cmp)

        """
        # you can draw the graph to see the whole structure
        nx.draw(g, with_labels=True)
        plt.show()
        """

        cuts = nx.minimum_edge_cut(g)
        g.remove_edges_from(cuts)
        groups = nx.connected_components(g)

        return math.prod(map(len, groups))

    def part2(self, data):
        return "HoHoHo"


input = [line.strip() for line in open('25.in')]
s = Solution()
print(s.part1(input))