#!/Users/gbolek/.pyenv/versions/raycastenv/bin/python
###!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title post to url
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description send to yggdrasil

import sys;
import requests;

print("Hello World!")
print(sys.version)
res = requests.get("http://some-url-here")
print(res)