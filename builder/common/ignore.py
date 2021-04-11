import builder

comment = f"Create By Builder ({builder.__homepage__})"
idea = [comment, '# IntelliJ project files', '.idea', '*.iml', 'out', 'gen']
python_ignore = ['### Python template', '# Byte-compiled / optimized / DLL files', '__pycache__/', '*.py[cod]',
                 '*$py.class', '', '# C extensions', '*.so', '', '# Distribution / packaging', '.Python', 'build/',
                 'develop-eggs/', 'dist.sh/', 'downloads/', 'eggs/', '.eggs/', 'lib/', 'lib64/', 'parts/', 'sdist/',
                 'var/',
                 'wheels/', 'share/python-wheels/', '*.egg-info/', '.installed.cfg', '*.egg', 'MANIFEST', 'dist', '',
                 '# PyInstaller', '#  Usually these files are written by a python script from a template',
                 '#  before PyInstaller builds the exe, so as to inject date/other infos into it.', '*.manifest',
                 '*.spec',
                 '', '# Installer logs', 'pip-log.txt', 'pip-delete-this-directory.txt', '',
                 '# Unit test / coverage reports', 'htmlcov/', '.tox/', '.nox/', '.coverage', '.coverage.*', '.cache',
                 'nosetests.xml', 'coverage.xml', '*.cover', '*.py,cover', '.hypothesis/', '.pytest_cache/', 'cover/',
                 '',
                 '# Translations', '*.mo', '*.pot', '', '# Django stuff:', '*.log', 'local_settings.py', 'db.sqlite3',
                 'db.sqlite3-journal', '', '# Flask stuff:', 'instance/', '.webassets-cache', '', '# Scrapy stuff:',
                 '.scrapy', '', '# Sphinx documentation', 'docs/_build/', '', '# PyBuilder', '.pybuilder/', 'target/',
                 '',
                 '# Jupyter Notebook', '.ipynb_checkpoints', '', '# IPython', 'profile_default/', 'ipython_config.py',
                 '',
                 '# pyenv', '#   For a library or package, you might want to ignore these files since the code is',
                 '#   intended to run in multiple environments; otherwise, check them in:', '# .python-version', '',
                 '# pipenv',
                 '#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.',
                 '#   However, in case of collaboration, if having platform-specific dependencies or dependencies',
                 "#   having no cross-platform support, pipenv may install dependencies that don't work, or not",
                 '#   install all needed dependencies.', '#Pipfile.lock', '',
                 '# PEP 582; used by e.g. github.com/David-OConnor/pyflow', '__pypackages__/', '', '# Celery stuff',
                 'celerybeat-schedule', 'celerybeat.pid', '', '# SageMath parsed files', '*.sage.py', '',
                 '# Environments',
                 '.env', '.venv', 'env/', 'venv/', 'ENV/', 'env.bak/', 'venv.bak/', '', '# Spyder project settings',
                 '.spyderproject', '.spyproject', '', '# Rope project settings', '.ropeproject', '',
                 '# mkdocs documentation', '/site', '', '# mypy', '.mypy_cache/', '.dmypy.json', 'dmypy.json', '',
                 '# Pyre type checker', '.pyre/', '', '# pytype static type analyzer', '.pytype/', '',
                 '# Cython debug symbols', 'cython_debug/', '']

java_ignore = ['# Compiled class file', '*.class', '', '# Log file', '*.log', '', '# BlueJ files', '*.ctxt', '',
               '# Mobile Tools for Java (J2ME)', '.mtj.tmp/', '', '# Package Files #', '*.jar', '*.war', '*.nar',
               '*.ear', '*.zip', '*.tar.gz', '*.rar', '',
               '# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml',
               'hs_err_pid*', '', '', 'target', '.mvn', 'mvnw', 'mvnw.cmd']

golang_ignore = ['# Binaries for programs and plugins', '*.exe', '*.exe~', '*.dll', '*.so', '*.dylib', 'pipeline', '',
                 '# Test binary, built with `go test -c`', '*.test', '',
                 '# Output of the go coverage tool, specifically when used with LiteIDE', '*.out', '',
                 '# Dependency directories (remove the comment below to include it)', '# vendor/', '']


def build_up_ignore(kind):
    result = idea
    if kind == "python":
        result.extend(python_ignore)
    elif kind == "spring":
        result.extend(java_ignore)
    elif kind == "golang":
        result.extend(golang_ignore)

    return "\n".join(result)
