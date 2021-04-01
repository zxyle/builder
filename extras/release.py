#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os

import oss2

from builder import __version__, __project__

env = dict()
with open("../.env") as f:
    lines = f.readlines()
    for line in lines:
        k, v = line.strip().split("=")
        env.update({k: v})

os.chdir("../../")
filename = f"{__project__}-{__version__}"
extension = ".tar.gz"


def package():
    cmd = f"tar -zcvf  {filename}{extension}"
    exclude_pattern = [
        f'{__project__}/venv',
        f'{__project__}/.git',
        f'{__project__}/.idea',
        f'{__project__}/__pycache__',
        f'{__project__}/.env',
        "'*.pyc'"
    ]

    for pattern in exclude_pattern:
        cmd += f" --exclude={pattern}"

    cmd += f" {__project__}"
    exit_code = os.system(cmd)
    print(exit_code)


def upload_oss():
    access_key_id = env.get("access_key_id")
    access_key_secret = env.get("access_key_secret")
    endpoint = env.get("endpoint")
    bucket_name = env.get("bucket_name")

    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    object_name = f'{filename}{extension}'
    with open(f'./{filename}{extension}', 'rb') as f:
        bucket.put_object(object_name, f)

    url = f"https://{bucket_name}.{endpoint}/{object_name}"
    print(f"  url \"{url}\"")

    hash_value = hash_file()
    print(f"  sha256 \"{hash_value}\"")


def hash_file():
    hasher = hashlib.sha256()

    with open(f'./{filename}{extension}', 'rb') as f:
        hasher.update(f.read())
        sha256 = hasher.hexdigest()
        return sha256


if __name__ == '__main__':
    package()
    upload_oss()
