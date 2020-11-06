===========================
pyupgrade-directories
===========================

.. start short_desc

**Run pyupgrade on all files in a directory, and optionally recursively.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| rtfd-shield::
	:project: pyupgrade-directories
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |travis| travis-shield::
	:travis-site: com
	:alt: Travis Build Status

.. |actions_windows| actions-shield::
	:workflow: Windows Tests
	:alt: Windows Tests Status

.. |actions_macos| actions-shield::
	:workflow: macOS Tests
	:alt: macOS Tests Status

.. |requires| requires-io-shield::
	:alt: Requirements Status

.. |codefactor| codefactor-shield::
	:alt: CodeFactor Grade

.. |pypi-version| pypi-shield::
	:project: pyupgrade-directories
	:version:
	:alt: PyPI - Package Version

.. |supported-versions| pypi-shield::
	:project: pyupgrade-directories
	:py-versions:
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| pypi-shield::
	:project: pyupgrade-directories
	:implementations:
	:alt: PyPI - Supported Implementations

.. |wheel| pypi-shield::
	:project: pyupgrade-directories
	:wheel:
	:alt: PyPI - Wheel

.. |license| github-shield::
	:license:
	:alt: License

.. |language| github-shield::
	:top-language:
	:alt: GitHub top language

.. |commits-since| github-shield::
	:commits-since: v0.0.3
	:alt: GitHub commits since tagged version

.. |commits-latest| github-shield::
	:last-commit:
	:alt: GitHub last commit

.. |maintained| maintained-shield:: 2020
	:alt: Maintenance

.. |pre_commit| pre-commit-shield::
	:alt: pre-commit

.. |pre_commit_ci| pre-commit-ci-shield::
	:alt: pre-commit.ci status

.. end shields

Installation
---------------

.. start installation

.. installation:: pyupgrade-directories
	:pypi:
	:github:

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


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	API Reference<docs>
	Source
	Building

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/pyupgrade-directories>`__

.. end links
