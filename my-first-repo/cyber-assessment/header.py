#!/usr/bin/python3
import sys
from urllib.request import urlopen

with urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))

