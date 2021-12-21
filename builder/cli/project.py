import os

import inquirer
from jinja2 import Environment, FileSystemLoader

from builder.cli.filters import string_camelcase, sanitize, underscore, passphrase
from builder.cli.git import git_init
from builder.cli.pom import properties, dependencies, Property
from builder.cli.utils import copytree, get_sys_user
from builder.common.ignore import build_up_ignore
from builder.common.license import choose
from builder.golang.utils import find_go_version


class Template:
    def __init__(self):
        pass

    def loads(self):
        pass

    def render(self):
        pass


def load_temps(dst):
    """
    加载指定目录的模板
    :param dst:
    :return:
    """
    extensions = "tmpl"
    env = Environment(
        loader=FileSystemLoader(dst)
    )

    # 自定义过滤器
    env.filters['camelcase'] = string_camelcase
    env.filters['sanitize'] = sanitize

    # 自定义函数
    env.globals['passphrase'] = passphrase

    return [env.get_template(t) for t in env.list_templates(extensions)]


def render_template_file(t, **kwargs):
    """
    渲染模板
    :param t: 模板
    :param kwargs: 元数据
    :return:
    """
    path = t.filename
    content = t.render(kwargs)

    render_path = path[:-len('.tmpl')] if path.endswith('.tmpl') else path

    if path.endswith('.tmpl'):
        os.rename(path, render_path)

    with open(render_path, 'wb') as fp:
        fp.write(content.encode('utf8'))


def recursive_delete(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            p = os.path.join(path, file)
            if os.path.isdir(p):
                recursive_delete(p)
            else:
                os.remove(p)
        os.rmdir(path)
    else:
        os.remove(path)


class Base:
    empty_files = []
    output_dir = ""
    root_dir = ""
    metadata = {}
    questions = []

    # 复制到目标目录
    # 渲染模板
    def copy_template(self, temp_name, dst, project_name):
        temps = [temp_name, "common"]
        target_dir = os.path.join(dst, project_name)
        # 复制模板目录到目标目录下
        for temp in temps:
            tempdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"templates/{temp}")
            copytree(tempdir, target_dir)

        self.output_dir = target_dir
        return target_dir

    def render(self, target_dir, args):
        # 遍历该目录下所有文件, 找到tmpl文件
        templates = load_temps(target_dir)

        # render
        for template in templates:
            render_template_file(template, **args)

    def after(self):
        self.touch_empty_files()
        author = self.metadata.get("author")
        license_kind = self.metadata.get("license")
        if license_kind and license_kind != "none":
            license_content = choose(author, license_kind)
            self.write("LICENSE", license_content)

        ignore_content = build_up_ignore(self.temp_name)
        self.write(".gitignore", ignore_content)
        if self.show("Do you need to git init this project?"):
            git_init(self.output_dir)

    def write(self, path, content):
        with open(f"{self.output_dir}/{path}", "w") as f:
            f.write(content)

    def docker_support(self):
        if self.show("🐳 Do you need docker support?"):
            self.empty_files.extend([
                "Dockerfile",
                "docker-compose.yml",
                ".dockerignore",
            ])

    def show(self, prompt):
        if input(f"{prompt} [Y/N]:").lower() != "n":
            return True
        return False

    def touch_empty_files(self):
        for file in self.empty_files:
            file_path = os.path.join(self.output_dir, file)
            dir_name = os.path.dirname(file_path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(file_path, 'w'):
                pass

    def input_prompt(self):
        # TODO
        # version
        # description
        # entry point (index.js)
        # test command
        # git repository
        # keywords
        # author
        # license: (ISC)
        answers = inquirer.prompt(self.questions)
        self.metadata.update(answers)


class SpringProject(Base):
    temp_name = "spring"
    questions = [
        inquirer.Text('group', message="Please enter a group", default="com.example"),
        inquirer.Text('artifact', message="Please enter a artifact", default="demo"),
        inquirer.Text('description', message="Please enter a description", default="Demo project for Spring Boot"),
        inquirer.Text('author', message="What's your name", default=get_sys_user()),
        inquirer.List('packaging',
                      message="packaging?",
                      choices=['jar', 'war'],
                      ),
        inquirer.List('javaVersion',
                      message="javaVersion?",
                      choices=['8', '11', '17'],
                      ),
        inquirer.List('bootVersion',
                      message="bootVersion?",
                      choices=['2.4.4', '2.6.1', '2.5.7'],
                      ),

        inquirer.List('license',
                      message="license?",
                      choices=['none', 'mit', 'apache'],
                      ),
        inquirer.List('Project',
                      message="project?",
                      choices=['Maven Project', 'Gradle Project'],
                      ),
        inquirer.List('Language',
                      message="Language?",
                      choices=['Java', 'Kotlin', 'Groovy'],
                      ),
    ]

    def copy_other(self, dst, group_path, artifact):
        target_dir = os.path.join(dst, artifact)
        for p in ["main", "test"]:
            _dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"templates/spring/{p}")
            copytree(_dir, f"{target_dir}/src/{p}/java/{group_path}/{sanitize(artifact)}")

    def run(self, dst):
        print("开始创建spring boot项目.")
        self.input_prompt()
        group = self.metadata.get("group")
        artifact = self.metadata.get("artifact")
        self.metadata.update({"projectName": artifact})
        base_package = f"{group}.{sanitize(artifact)}"
        java_version = self.metadata.get("javaVersion")
        properties.extend([
            Property("maven.compiler.source", java_version),
            Property("maven.compiler.target", java_version),
            Property("maven.compiler.compilerVersion", java_version),
            Property("java.version", java_version),
        ])
        self.metadata.update({
            "properties": properties,
            "dependencies": dependencies,
            "basePackage": base_package,
            "dbName": underscore(artifact),
            "bootVersion": self.metadata.get("bootVersion"),
        })

        self.empty_files.extend([
            "docs/代码规范.md",
        ])

        dst = os.getcwd() if dst == "." else dst
        group_path = "/".join(group.split("."))
        self.copy_other(dst, group_path, artifact)

        target_dir = self.copy_template(self.temp_name + "/root", dst, artifact)
        self.render(target_dir, self.metadata)

        app_name = string_camelcase(artifact)
        main_dir = f"{target_dir}/src/main/java/{group_path}/{app_name}"
        test_dir = f"{target_dir}/src/test/java/{group_path}/{app_name}"

        os.rename(f"{main_dir}/DemoApplication.java",
                  f"{main_dir}/{app_name}Application.java")
        os.rename(f"{test_dir}/DemoApplicationTests.java",
                  f"{test_dir}/{app_name}ApplicationTests.java")
        self.after()

    def clean(self):
        pass


class PythonProject(Base):
    temp_name = "python"
    questions = [
        inquirer.Text('projectName', message="Please enter a projectName", default="awesome"),
        inquirer.Text('author', message="What's your name", default=get_sys_user()),
        inquirer.List('license',
                      message="license?",
                      choices=['none', 'mit', 'apache'],
                      ),
    ]

    def run(self, dst):
        self.input_prompt()
        project_name = self.metadata.get("projectName")
        target_dir = self.copy_template(self.temp_name, dst, project_name)
        self.render(target_dir, self.metadata)
        self.docker_support()
        self.empty_files.extend([
            "requirements.txt",
            "setup.cfg",
            "tests/__init__.py",
            f"{project_name}/__init__.py",
            "scripts/__init__.py",
            "docs/guide.md",
            "docs/TODO.md",
        ])
        self.after()


class FlaskProject(Base):
    temp_name = "flask"


class GolangProject(Base):
    temp_name = "golang"
    questions = [
        inquirer.Text('projectName', message="Please enter a projectName", default="awesome"),
        inquirer.Text('goVersion', message="Please enter a goVersion", default=find_go_version()),
        inquirer.Text('author', message="What's your name", default=get_sys_user()),
        inquirer.List('license',
                      message="license?",
                      choices=['none', 'mit', 'apache'],
                      ),
    ]

    def run(self, dst):
        self.input_prompt()
        project_name = self.metadata.get("projectName")
        target_dir = self.copy_template(self.temp_name, dst, project_name)
        self.render(target_dir, self.metadata)
        self.docker_support()
        self.empty_files.extend([
            "docs/guide.md",
            "docs/TODO.md",
            "go.sum",
        ])
        self.after()


class GitbookProject(Base):
    temp_name = "gitbook"
    metadata = {
        "projectName": "awesome",
    }
    questions = [
        inquirer.Text('projectName', message="Please enter a projectName", default="awesome"),
    ]

    def run(self, dst):
        self.input_prompt()
        project_name = self.metadata.get("projectName")
        target_dir = self.copy_template(self.temp_name, dst, project_name)
        self.render(target_dir, self.metadata)
        self.after()


class UmiProject(Base):
    temp_name = "umi"
    questions = [
        inquirer.Text('projectName', message="Please enter a projectName", default="awesome"),
    ]

    def run(self, dst):
        self.input_prompt()
        project_name = self.metadata.get("projectName")
        target_dir = self.copy_template(self.temp_name, dst, project_name)
        self.render(target_dir, self.metadata)
        self.after()
