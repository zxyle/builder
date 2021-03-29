import os


# TODO ignore
from builder import version


def git_init(dst):
    os.chdir(dst)
    # 检查git命令是否存在
    exit_code = os.system("git version")
    if exit_code == 0:
        # git config --global --get user.name
        # git config --global --get user.email

        # git config --local user.name ""
        # git config --local user.email ""

        # git config --global user.email "you@example.com"
        # git config --global user.name "Your Name"

        os.system("git init")
        os.system("git add .")
        message = f"first commit by builder, version: {version}"
        os.system(f'git commit -m "{message}"')

        # TODO add remote and push

        os.system("git checkout -b develop")
    else:
        print("git command not found")


def gitflow():
    pass


class IgnoreFile:
    pass


class GitIgnore(IgnoreFile):
    pass


class DockerIgnore(IgnoreFile):
    pass


class GitRepository:

    def __init__(self, dst):
        self.dst = dst

    def git_init(self):
        pass

    def add(self):
        pass

    def push(self):
        pass

    def commit(self):
        pass

    def remote(self, name, url):
        pass
