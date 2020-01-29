```python
import tivo
```

# TiVo Examples

Higher level wrapper [```mattjgalloway```'s python-tivo]. Attempts to be more pythonic and less verbose. ```TiVo module for humans```.




```python
tivo_cfg = {
    "host": "192.168.1.135",
    "port": 31339,
}
# Low Level
c=tivo.connection.TiVoConnection(**tivo_cfg)
# High Level
t=tivo.TiVo(**tivo_cfg)
```

## Watch LiveTV



```python
# Low Level
c.sendIRCode("LIVETV")
```




    [{'raw': 'CH_STATUS 0287 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0287',
      'reason': 'LOCAL',
      'subChannel': None},
     {'raw': 'CH_STATUS 0233 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'LOCAL',
      'subChannel': None},
     {'raw': 'CH_STATUS 0233 RECORDING',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'RECORDING',
      'subChannel': None}]




```python
# High Level.
t.livetv()
```




    [{'raw': 'CH_STATUS 0233 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'LOCAL',
      'subChannel': None},
     {'raw': 'CH_STATUS 0232 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0232',
      'reason': 'LOCAL',
      'subChannel': None}]



## Send Multiple Commands.

Cheat codes for your TiVo.

## High Level


```python
# Low Level
for cmd in ["LIVETV", "TIVO", "RIGHT", "RIGHT", "RIGHT", "SELECT"]:
    c.sendIRCode(cmd)
```


```python
# High Level
t.combo(["livetv", "tivo", "right", "right", "right", "select"]);
```

## Send a String


```python
# Low Level
for char in "HELLO":
    c.sendKeyboard(char)
```


```python
# High Level
t.send_str(" WORLD")
```




    [{'raw': 'CH_STATUS 0233 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'LOCAL',
      'subChannel': None}]



## Set the current channel

Manually types out the channel and presses enter. ```SETCH``` does not work on all TiVo boxes.


```python
# Low Level
c.sendCommands(["IRCODE LIVETV", "IRCODE NUM2", "IRCODE NUM4", "IRCODE NUM0", "IRCODE ENTER"])
```




    [{'raw': 'CH_STATUS 0233 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'LOCAL',
      'subChannel': None},
     {'raw': 'CH_STATUS 0240 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0240',
      'reason': 'LOCAL',
      'subChannel': None}]




```python
# High Level
t.chan=231
```


```python
# High Level
t.chan=233
```


```python
t.back()
```




    [{'raw': 'CH_STATUS 0233 LOCAL',
      'type': 'CH_STATUS',
      'channel': '0233',
      'reason': 'LOCAL',
      'subChannel': None}]




```python

```
