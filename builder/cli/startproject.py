import importlib
import os
import sys


def to_list():
    root = os.path.dirname((os.path.dirname(__file__)))
    temp_dir = os.path.join(root, "templates")
    return os.listdir(temp_dir)


def create(temp_name, dst):
    # 检查templates目录下有没有对应的目录
    if temp_name not in to_list():
        print(f"无该{temp_name}模板项目.")
        sys.exit(0)

    model = importlib.import_module("builder.cli.project")
    class_name = f"{temp_name.capitalize()}Project"
    clazz = getattr(model, class_name)
    if not clazz:
        print(f"No {temp_name} template!")
        sys.exit(2)

    instance = clazz()
    instance.run(dst)

    print(f"创建{temp_name}项目完成, 在\"{instance.output_dir}\".")


if __name__ == '__main__':
    # create("python", "/Users/xiangzheng/developer/projects/personal/")
    create("spring", "/Users/xiangzheng/developer/projects/personal/")
    # create("golang", "/Users/xiangzheng/developer/projects/personal/")
    # create("python", "/Users/xiangzheng/developer/projects/personal/")
