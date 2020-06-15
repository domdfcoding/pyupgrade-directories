==========================
pyupgrade-directories
==========================

.. start short_desc

**Run pyupgrade on all files in a directory, and optionally recursively.**

.. end short_desc


.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs|
	* - Tests
	  - |travis| |requires| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Other
	  - |license| |language| |commits-since| |commits-latest| |maintained| 

.. |docs| image:: https://img.shields.io/readthedocs/pyupgrade-directories/latest?logo=read-the-docs
	:target: https://pyupgrade-directories.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/pyupgrade-directories/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/pyupgrade-directories
	:alt: Travis Build Status

.. |requires| image:: https://requires.io/github/domdfcoding/pyupgrade-directories/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/pyupgrade-directories/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/pyupgrade-directories?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/pyupgrade-directories
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/pyupgrade-directories
	:alt: License
	:target: https://github.com/domdfcoding/pyupgrade-directories/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/pyupgrade-directories
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/pyupgrade-directories/v0.0.3
	:target: https://github.com/domdfcoding/pyupgrade-directories/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/pyupgrade-directories
	:target: https://github.com/domdfcoding/pyupgrade-directories/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields


Installation
--------------

.. start installation

``pyupgrade-directories`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install pyupgrade-directories

.. end installation


Usage
--------------

``pyupgrade-directories`` is called from the command line with ``pyup_dirs``.

Basic usage is the same as ``pyupgrade``.
See https://github.com/asottile/pyupgrade/blob/master/README.md for more information.

The key difference is that passing a directory to ``pyup_dir`` will process all ``.py`` files in the directory.
There is also ``--recursive`` flag that will recurse subdirectories.

Any ``.pyd``, ``.pyc`` and ``.pyo`` files are excluded, along with any files in
``__pycache__``, ``.tox``, ``.mypy_cache``, ``.pytest_cache`` and ``venv`` directories.
