import os


def find_go_version():
    exit_code = os.system("go version")
    if exit_code != 0:
        print(" golang is not installed.")


if __name__ == '__main__':
    find_go_version()