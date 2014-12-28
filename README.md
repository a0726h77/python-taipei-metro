## Dependencies

```
make install-dependencies
```

## Usage

```
./metro 圓山 忠孝復興
```

```
>>> from rapid.systems import TaipeiMetro
>>> metro = TaipeiMetro()
>>> metro.show_map()
>>> metro.search_routes('圓山', '忠孝復興', 1)
```

## API

```
>>> from rapid.systems import TaipeiMetro
>>> metro = TaipeiMetro()
>>> metro.system.get_lines()
>>> metro.system.get_line_stations('淡水信義線')
>>> metro.system.get_map()
>>> metro.system.get_routes('圓山', '忠孝復興', 1)
```

## Screenshot
![alt tag](https://raw.githubusercontent.com/a0726h77/python-taipei-metro/master/screenshot/2014-12-28-152339_1366x768_scrot.png)
