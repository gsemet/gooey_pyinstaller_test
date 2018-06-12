# coding: utf-8

import pbr.version

from gooey_pyinstaller_test._gooey_pyinstaller_test import MyPublicClass


def version():
    return pbr.version.VersionInfo('gooey_pyinstaller_test').release_string()

## Uncomment the following line to declare a __version__ in your root module. Beware the evaluation
## of the version may impact the load time of your module
#
# __version__ = version()
#
#
__all__ = [
    'version',
    'MyPublicClass',
]
