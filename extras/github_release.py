#!/usr/bin/env python3

import hashlib

import requests

hasher = hashlib.sha256()

download_url = "https://github.com/zxyle/builder/archive/refs/tags/v0.0.1.zip"
hasher.update(requests.get(download_url).content)

sha256 = hasher.hexdigest()
print(sha256)
