import os

DEFAULT_GO_VERSION = "1.16"


def find_go_version():
    exit_code = os.system("go version")
    if exit_code != 0:
        print(" go is not installed.")

    return DEFAULT_GO_VERSION


if __name__ == '__main__':
    find_go_version()
