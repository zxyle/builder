import os


# TODO ignore


def git_init(dst):
    # 检查git命令是否存在
    os.chdir(dst)
    # git config --global user.email "you@example.com"
    # git config --global user.name "Your Name"
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "first commit"')

    # TODO add remote and push

    os.system("git checkout -b develop")


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
