#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../rapid/lib'))

from RouteMap import RouteMap


class SimplisticTest(unittest.TestCase):
    def setUp(self):
        self.route_map = RouteMap()
        self.route_map.update_graph([1, 3, 4, 5, 7, 2])

    def test_get_routes(self):
        self.assertEqual(self.route_map.get_routes(4, 2), [[4, 5, 7, 2]])
