import os
from shutil import ignore_patterns, copy2, copystat
from stat import S_IWUSR as OWNER_WRITE_PERMISSION

IGNORE = ignore_patterns('*.pyc', '__pycache__', '.svn')


def _make_writable(path):
    current_permissions = os.stat(path).st_mode
    os.chmod(path, current_permissions | OWNER_WRITE_PERMISSION)


def copytree(src, dst):
    ignore = IGNORE
    names = os.listdir(src)
    ignored_names = ignore(src, names)

    if not os.path.exists(dst):
        os.makedirs(dst)

    for name in names:

        if name in ignored_names:
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if os.path.isdir(srcname):
            copytree(srcname, dstname)
        else:
            copy2(srcname, dstname)
            _make_writable(dstname)

    copystat(src, dst)
    _make_writable(dst)
