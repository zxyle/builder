#!/usr/bin/env bash


function install() {
    rm -rf build/ builder.egg-info/ dist/
    package
    pip uninstall -y builder
    pip install dist/builder-0.0.1-py3-none-any.whl
}

function package() {
    python3 setup.py sdist bdist_wheel
}


function publish() {
   pip install -U wheel twine setuptools
   package
   twine upload dist/*
}

function usage() {
    echo "Usage: sh dist.sh [install|publish]"
    exit 1
}

function test() {
    echo "TEST"
    exit 0
}

#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
  "install")
    install
    ;;
  "package")
    package
    ;;
  "publish")
    publish
    ;;
  *)
    usage
    ;;
esac