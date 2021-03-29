# https://pypi.org/project/builder/

from os.path import abspath, dirname, join

from setuptools import find_packages, setup

from builder import version

install_reqs = [req.strip() for req in open(abspath(join(dirname(__file__), 'requirements.txt')))]

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="builder",
    version=version,
    author="Xiang Zheng",
    author_email="zxyful@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/zxyle/builder",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_reqs,
    # tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'builder = builder.cli.main:main',
        ],
    },
    # https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
