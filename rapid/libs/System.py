#!/usr/bin/env python
# encoding: utf-8

import uuid
from rapid.libs.RouteMap import RouteMap


class System():
    def __init__(self):
        self.map = {}
        self._line_ids = {}
        self.route_map = RouteMap()

    def add_line(self, name):
        if name not in self._line_ids.keys():
            id = str(uuid.uuid4())

            self._line_ids[name] = id

            line_structure = {'name': name, 'stations': []}
            self.map[id] = line_structure

            return id
        else:
            return self._line_ids[name]

    def get_lines(self):
        return [l for l in sorted(self._line_ids)]

    def add_line_stations(self, name, stations):
        # 新增路線
        self.add_line(name)

        # 新增節點
        if isinstance(stations, list):
            self.map[self._line_ids[name]]['stations'] = self.map[self._line_ids[name]]['stations'] + stations
        else:
            self.map[self._line_ids[name]]['stations'].append(stations)

        # 更新 Graph
        self.route_map.update_graph(stations)

    def get_line_stations(self, name):
        return self.map[self._line_ids[name]]['stations']

    # 尋找兩臨近站點所在線路
    def get_station_line(self, station_a, station_b):
        stations = (station_a, station_b)

        for id, line in self.map.items():
            # if station_a in line['stations'] and station_b in line['stations']:
            if all((n in line['stations'] for n in stations)):
                return line['name']

    def get_map(self):
        '''
        [{'name': 'Line_1', 'stations': ['a', 'b', 'c']}, ...]
        '''
        return sorted([v for k, v in self.map.items()], key=lambda x: (x['name']))

    def count_transfer(self, stations):
        lines = []

        # 計算節點經過的所有路線
        for index in range(0, len(stations)-1):
            # print '%s %s %s' % (stations[index], stations[index+1], self.get_station_line(stations[index], stations[index+1]))
            lines.append(self.get_station_line(stations[index], stations[index+1]))

        # 移除陣列重複元素
        # ['淡水信義線', '中和新蘆線', '中和新蘆線', '板南線'] => ['淡水信義線', '中和新蘆線', '板南線']
        lines = list(set(lines))

        # 扣除出發的線路
        return len(lines) - 1

    def get_routes(self, station_a, station_b, lines=5):
        # get all routes
        routes = self.route_map.get_routes(station_a, station_b)

        # 計算每條路徑所經過的節點數,及轉乘次數
        # [ {'index': 0, 'count': 7, 'transfer': 3}, {'index': 1, 'count': 7, 'transfer': 2}, {'index': 2, 'count': 8, 'transfer': 1}, ... ]
        path_detail = []
        for index in range(0, len(routes)):
            _ = {}

            _['index'] = index
            _['count'] = len(routes[index])
            _['transfer'] = self.count_transfer(routes[index])
            _['route'] = routes[index]

            path_detail.append(_)

        # 依照路徑經過節點數及轉乘次數排序
        # [ {'index': 1, 'count': 7, 'transfer': 2}, {'index': 0, 'count': 7, 'transfer': 3}, {'index': 2, 'count': 8, 'transfer': 1}, ... ]
        path_detail_ordered = sorted(path_detail, key=lambda x: (x['count'], x['transfer']))

        # 回傳前幾條路徑
        if lines > len(routes):
            lines = len(routes)
        return path_detail_ordered[0:lines]
