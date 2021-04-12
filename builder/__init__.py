import sys

python_version = sys.version_info

__author__ = "Xiang Zheng"
__email__ = "zxyful@gmail.com"
__version__ = "0.0.1"
__project__ = "builder"
__description__ = "Quickly create batteries included project"
__homepage__ = "https://github.com/zxyle/builder"
__license__ = "MIT"
__repository__ = f"{__homepage__}.git"
__python_version__ = f"{python_version[0]}.{python_version[1]}"

if sys.version_info[0] < 3:
    raise ImportError('Python < 3 is unsupported.')
