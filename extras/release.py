#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib

from builder import __version__, __project__

# 打包整个source code tar.gz
# builder-0.0.1.tar


project = "bu"
os.chdir("../../")

filename = f"{__project__}-{__version__}"

cmd = f"tar -zcvf  {filename}.tar.gz"

exclude_pattern = [
    f'{__project__}/venv',
    f'{__project__}/.idea',
    f'{__project__}/__pycache__',
    "'*.pyc'"
]

for pattern in exclude_pattern:
    cmd += f" --exclude={pattern}"

cmd += f" {__project__}"
exit_code = os.system(cmd)
print(exit_code)

# 上传至oss上

# 打印sha256和下载路径
hasher = hashlib.sha256()

# with open('') as f:
#     f.read()
#     hasher.update()
#     sha256 = hasher.hexdigest()
#     print(sha256)




