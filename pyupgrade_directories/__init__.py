#!/usr/bin/env python3
#
#  __init__.py
"""
Run pyupgrade on all files in a directory, and optionally recursively.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  MIT Licensed
#

# stdlib
import pathlib
from typing import Iterable, List

__all__ = ["iter_py_files"]

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"
__license__ = "MIT"
__version__ = "0.1.1"
__email__ = "dominic@davis-foster.co.uk"


def iter_py_files(files_and_dirs: Iterable[pathlib.Path], recursive: bool = False) -> Iterable[pathlib.Path]:
	"""
	Iterate over all ``.py`` files in the given directories.

	TODO: Wildcards in filename/directory

	:param files_and_dirs: An iterable of filenames and directories
	:param recursive: Whether subdirectories should be recursed. Default :py:obj:`False`
	:type recursive: bool
	"""

	all_py_files: List[pathlib.Path] = []

	for filename in files_and_dirs:

		if filename.suffix.startswith(".py") and filename.is_file():
			all_py_files.append(filename)

		elif filename.is_dir():
			if recursive:
				all_py_files += list(filename.rglob("*.py*"))
			else:
				all_py_files += list(filename.rglob("*.py*"))

	for filename in all_py_files:
		if not filename.is_file():
			continue

		if not filename.suffix.startswith(".py"):
			continue

		if filename.suffix in {".pyd", ".pyc", ".pyo"}:
			continue

		filename = filename.absolute()

		if any(
				exclude_dir in str(filename.parent)
				for exclude_dir in {".mypy_cache", ".pytest_cache", "venv", ".tox", "__pycache__"}
				):
			continue

		yield filename
