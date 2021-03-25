import sys

from builder.cli.startproject import create

# 读取命令行输入
# argparse
# python-fire
# click
# typer


def main():
    args = sys.argv
    if len(args) == 1:
        print("使用方法: builder spring .")
        sys.exit(0)
    elif len(args) == 2:
        # builder springboot
        _, option = args
        create(option, ".")
    elif len(args) == 3:
        # builder springboot ~/Download/projects
        _, option, dst = args
        create(option, dst)
