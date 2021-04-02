# https://pypi.org/project/builder/

from os.path import abspath, dirname, join

from setuptools import find_packages, setup

import builder

install_reqs = [req.strip() for req in open(abspath(join(dirname(__file__), 'requirements.txt')))]

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="builder",
    version=builder.__version__,
    author=builder.__author__,
    author_email=builder.__email__,
    description=builder.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=builder.__license__,
    url=builder.__homepage__,
    packages=find_packages(),
    # download_url="",
    # package_data=None,
    # data_files=None,
    # keywords=None,
    # project_urls=None,
    # py_modules=None,
    # python_requires=None,
    # scripts=None,
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
