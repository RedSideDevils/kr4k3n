# Kr4k3n Backdoor Tool
 Backdoor with main functions.

## How it works
```
1) Run kr4k3n.py and generate target file with IP and PORT.
2) Run kr4k3n.py and wait until target connection. 
3) Use kraken-help command to see functions.
```

![](https://j.gifs.com/jZoEJB.gif)

## Features
- Multi-threading
- Completely Automated
- Takes list from file

## Installation:
One line installation:
```
$ git clone https://github.com/DreyAnd/DeadDNS.git && cd DeadDNS && pip3 install -r requirements.txt
```

Simple and quick installation:
```
$ git clone https://github.com/DreyAnd/DeadDNS.git
$ cd DeadDNS
$ pip3 install -r requirements.txt
```

## Usage:

Example usage:
```
$ python3 dead_records.py -w subdomains.txt -o1 dead.txt -o2 cname.txt
```

This will return all output to stdout without saving it.

Help: `$ python3 dead_records.py -h`

To check progress do `tail -f dead-temp.txt` and `tail -f cname-temp.txt`

## Made with :heart: by [DreyAnd](https://github.com/DreyAnd) and [inc0gnit0](https://github.com/iinc0gnit0)

