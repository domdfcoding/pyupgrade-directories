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

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/pyupgrade-directories/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/pyupgrade-directories/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/pyupgrade-directories/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/pyupgrade-directories/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/pyupgrade-directories/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/pyupgrade-directories/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/pyupgrade-directories/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/pyupgrade-directories/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/pyupgrade-directories/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/pyupgrade-directories/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/domdfcoding/pyupgrade-directories/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/pyupgrade-directories/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/pyupgrade-directories?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/pyupgrade-directories
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyupgrade-directories?logo=python&logoColor=white
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/pyupgrade-directories
	:target: https://github.com/domdfcoding/pyupgrade-directories/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/pyupgrade-directories
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/pyupgrade-directories/v0.1.1
	:target: https://github.com/domdfcoding/pyupgrade-directories/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/pyupgrade-directories
	:target: https://github.com/domdfcoding/pyupgrade-directories/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/pyupgrade-directories
	:target: https://pypi.org/project/pyupgrade-directories/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/pyupgrade-directories/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/pyupgrade-directories/master
	:alt: pre-commit.ci status

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
