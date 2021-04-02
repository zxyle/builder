#!/usr/bin/env python3
"""
Generate Ruby code with URLs and file hashes for packages from PyPi
(i.e., builder itself as well as its dependencies) to be included
in the Homebrew formula after a new release of Builder has been published
on PyPi.
<https://github.com/zxyle/homebrew-taps/blob/master/Formula/builder.rb>
"""

import hashlib
import os

import oss2
import requests

from builder import __version__, __project__, __description__, __homepage__, __license__, __python_version__

VERSIONS = {
    # By default, we use the latest packages. But sometimes Requests has a maximum supported versions.
    # Take a look here before making a release: <https://github.com/psf/requests/blob/master/setup.py>
}

DEPENDENCIES = [
    'urllib3',
    'idna',
    'chardet',
    'certifi',
    'requests',
    'MarkupSafe',
    'Jinja2'
]

MIRROR = "mirrors.cloud.tencent.com/pypi"


def get_package_meta(package_name):
    api_url = f'https://pypi.org/pypi/{package_name}/json'
    resp = requests.get(api_url).json()
    hasher = hashlib.sha256()
    version = VERSIONS.get(package_name)
    if package_name not in VERSIONS:
        # Latest version
        release_bundle = resp['urls']
    else:
        release_bundle = resp['releases'][version]

    for release in release_bundle:
        download_url = release['url']
        if download_url.endswith('.tar.gz'):
            download_url = download_url.replace("files.pythonhosted.org", MIRROR)
            hasher.update(requests.get(download_url).content)
            return {
                'name': package_name,
                'url': download_url,
                'sha256': hasher.hexdigest(),
            }
    else:
        raise RuntimeError(f'{package_name}: download not found: {resp}')


def main():
    package_meta_map = {
        package_name: get_package_meta(package_name)
        for package_name in DEPENDENCIES
    }

    print()
    print(f"  depends_on \"python@{__python_version__}\"")
    print()

    for dep_meta in package_meta_map.values():
        print('  resource "{name}" do'.format(name=dep_meta['name']))
        print('    url "{url}"'.format(url=dep_meta['url']))
        print('    sha256 "{sha256}"'.format(sha256=dep_meta['sha256']))
        print('  end')
        print('')


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


def upload_oss():
    access_key_id = env.get("access_key_id")
    access_key_secret = env.get("access_key_secret")
    endpoint = env.get("endpoint")
    bucket_name = env.get("bucket_name")

    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    object_name = f'{filename}{extension}'
    file = f'./{filename}{extension}'
    with open(file, 'rb') as f:
        pass
        # bucket.put_object(object_name, f)

    url = f"https://{bucket_name}.{endpoint}/{object_name}"
    print(f"  url \"{url}\"")

    hash_value = hash_file(file)
    print(f"  sha256 \"{hash_value}\"")
    print(f"  license \"{__license__}\"")


def hash_file(file):
    hasher = hashlib.sha256()

    with open(file, 'rb') as f:
        hasher.update(f.read())
        sha256 = hasher.hexdigest()
        return sha256


def print_metadata():
    print("class Builder < Formula")
    print("  include Language::Python::Virtualenv")
    print()
    print(f"  desc \"{__description__}\"")
    print(f"  homepage \"{__homepage__}\"")


def build_bottle():
    pass


if __name__ == '__main__':
    package()
    print_metadata()
    upload_oss()
    main()
