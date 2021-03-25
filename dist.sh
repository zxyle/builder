#!/usr/bin/env bash

rm -rf build/ builder.egg-info/ dist/
python3 setup.py sdist bdist_wheel
pip uninstall builder
pip install dist/builder-0.0.1-py3-none-any.whl