#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import unittest

sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../rapid/libs'))

from System import System


class SimplisticTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_add_lines(self):
        self.assertIsInstance(self.system.add_line('DanShui'), str)
        self.assertIsInstance(self.system.add_line('XinLu'), str)

    def test_get_lines(self):
        self.test_add_lines()
        self.assertIsInstance(self.system.get_lines(), list)
        self.assertEqual(len(self.system.get_lines()), 2)

    def test_add_line_stations(self):
        self.assertIsNone(self.system.add_line_stations('DanShui', ['YuanShan', 'MinQuanXiLu', 'ShuangLian', 'ZhongShan']))
        self.assertIsNone(self.system.add_line_stations('XinLu', ['DaQiaoTou', 'MinQuanXiLu', 'ZhongShanGuoXiao']))

    def test_get_station_line(self):
        self.test_add_line_stations()
        self.assertEqual(self.system.get_station_line('YuanShan', 'MinQuanXiLu'), 'DanShui')
        self.assertEqual(self.system.get_station_line('MinQuanXiLu', 'ZhongShanGuoXiao'), 'XinLu')

    def test_get_line_stations(self):
        self.test_get_station_line()
        self.assertIsInstance(self.system.get_line_stations('DanShui'), list)
        self.assertEqual(len(self.system.get_line_stations('DanShui')), 4)

    def test_get_map(self):
        self.test_get_line_stations()
        self.assertIsInstance(self.system.get_map(), list)
        self.assertEqual(len(self.system.get_map()), 2)

    def test_count_transfer(self):
        self.test_get_station_line()
        self.assertEqual(self.system.count_transfer(['YuanShan', 'MinQuanXiLu', 'ZhongShanGuoXiao']), 1)

    def test_get_route(self):
        self.test_count_transfer()
        self.assertIsInstance(self.system.get_routes('YuanShan', 'ZhongShanGuoXiao'), list)
        self.assertEqual(len(self.system.get_routes('YuanShan', 'ZhongShanGuoXiao')), 1)
