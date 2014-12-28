#!/usr/bin/env python
# encoding: utf-8

import networkx as nx
import uuid


class RouteMap(object):
    def __init__(self):
        self._graph = nx.Graph()

    def update_graph(self, nodes):
        self._graph.add_nodes_from(nodes)
        self._graph.add_edges_from(self._generate_edge_pair(nodes))

    def get_routes(self, node_a, node_b):
        routes = nx.all_simple_paths(self._graph, node_a, node_b)
        return [p for p in routes]

    def _generate_edge_pair(self, node_list):
        """
        >>> self._generate_edge_pair([1, 2, 3, 4])
        [(1, 2), (2, 3), (3, 4)]
        """
        edge_pairs = []

        for i in range(0, len(node_list)-1):
            edge_pairs.append((node_list[i], node_list[i+1]))

        return edge_pairs
