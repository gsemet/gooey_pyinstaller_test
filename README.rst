========
Overview
========

.. image:: https://travis-ci.org/gsemet/gooey_pyinstaller_test.svg?branch=master
    :target: https://travis-ci.org/gsemet/gooey_pyinstaller_test
.. image:: https://readthedocs.org/projects/gooey_pyinstaller_test/badge/?version=latest
   :target: http://gooey_pyinstaller_test.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/gsemet/gooey_pyinstaller_test/badge.svg
   :target: https://coveralls.io/github/gsemet/gooey_pyinstaller_test
.. image:: https://badge.fury.io/py/gooey_pyinstaller_test.svg
   :target: https://pypi.python.org/pypi/gooey_pyinstaller_test/
   :alt: Pypi package
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: ./LICENSE
   :alt: MIT licensed

Short Description of My Library

* Free software: MIT
* Documentation: https://gooey_pyinstaller_test.readthedocs.org/en/latest/
* Source: https://github.com/gsemet/gooey_pyinstaller_test

Features
--------

* TODO

Usage
-----

* TODO


Note: See `pipenv documentation <https://github.com/kennethreitz/pipenv>`_ for Pipfile
specification.

Contributing
------------

Setup for development:

    .. code-block:: bash

        $ make dev

Activate the virtualenv:

    .. code-block:: bash

        $ make shell  # equivalent to `pipenv shell`

Execute unit tests:

    .. code-block:: bash

        $ make test-unit


Build source package:

    Use it for most package without low level system dependencies.

    .. code-block:: bash

        make sdist

Build binary package:

    Needed for package with a C or other low level source code.

    .. code-block:: bash

        make bdist

Build Wheel package:

    Always provide a wheel package.

    .. code-block:: bash

        make wheel

To register Pipy deployment:

- commit your work!
- enable your project on Travis
- execute ``pipenv run python travis_pypi_setup.py``
- the ``.travis.yml`` is rewritten, you may want to restore its formatting.

Create a release:

    .. code-block:: bash

        make tag-pbr
        make push

On successful travis build on the Tag branch, your Pypi package will be updated automatically.

Configuration
-------------

You will need to configure `.travis.yml` to enable automatic PyPi deployment, or use the provided
`travis_pypi_setup.py` script. Beware your Yaml file will be overwritten, you will have to set the
format back manually.
