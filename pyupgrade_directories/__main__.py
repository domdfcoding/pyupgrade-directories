#!/usr/bin/env python3
#
#  __main__.py
"""
Run pyupgrade on all files in a directory, and optionally recursively.
"""
#
#  Copyright (c) 2020-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Based on pyupgrade
#  https://github.com/asottile/pyupgrade
#  Copyright (c) 2017 Anthony Sottile
#  MIT Licensed
#

# stdlib
import argparse
import pathlib
import sys
from typing import Optional, Sequence

# this package
from pyupgrade_directories import iter_py_files

try:
	# < 2.8.0

	# 3rd party
	from pyupgrade import main as _pyup_main  # type: ignore

except ImportError:
	# 2.8.0+

	# 3rd party
	from pyupgrade._main import main as _pyup_main  # type: ignore

__all__ = ["main"]


def main(argv: Optional[Sequence[str]] = None) -> int:
	"""
	Entry point for ``pyupgrade_directories``.
	"""

	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("filenames", nargs='*', type=pathlib.Path)
	parser.add_argument("--recursive", action="store_true", help="recurse subdirectories")

	args, argv = parser.parse_known_args(argv)

	return _pyup_main([*map(str, iter_py_files(args.filenames, args.recursive)), *argv])


if __name__ == "__main__":
	sys.exit(main())
