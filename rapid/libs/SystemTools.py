#!/usr/bin/env python
# encoding: utf-8

from rapid.libs.System import System


def list_2_string(array):
    return ', '.join(array)


class SystemTools():
    def __init__(self, LINE_NODES):
        self.LINE_NODES = LINE_NODES
        self.system = System()

        for name, nodes in self.LINE_NODES.items():
            self.system.add_line_stations(name, nodes)

    def show_map(self):
        for line in self.system.get_map():
            print("%s : [%s]" % (line['name'], list_2_string(line['stations'])))

    def show_lines(self):
        print(list_2_string(self.system.get_lines()))

    def show_line_stations(self, name):
        print(list_2_string(self.system.get_line_stations(name)))

    def search_routes(self, depart, arrive, lines=5, max_transfer=None):
        for route in self.system.get_routes(depart, arrive, lines, max_transfer):
            print("經過站數：%2d, 轉乘次數：%d\t%s" % (route['count'], route['transfer'], list_2_string(route['route'])))
