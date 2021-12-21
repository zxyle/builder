import os
import re

DEFAULT_GO_VERSION = "1.16"


def find_go_version():
    cmd = os.popen("go version")
    pattern = re.compile(r"\d+\.\d+\.\d+")
    text = cmd.read()
    match = pattern.search(text)
    if match:
        major, minor, micro = match.group().split(".")
        version = f"{major}.{minor}"
        return version

    return DEFAULT_GO_VERSION
