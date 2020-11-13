#!/usr/bin/env python3
#
#  __main__.py
"""
Run pyupgrade on all files in a directory, and optionally recursively.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Based on pyupgrade
#  https://github.com/asottile/pyupgrade
#  Copyright (c) 2017 Anthony Sottile
#  MIT Licensed
#

# stdlib
import argparse
import pathlib
from typing import Optional, Sequence

# 3rd party
from pyupgrade import _fix_file  # type: ignore

# this package
from pyupgrade_directories import iter_py_files

__all__ = ["main"]


def main(argv: Optional[Sequence[str]] = None) -> int:
	"""
	Entry point for ``pyupgrade_directories``.

	:rtype: int
	"""

	parser = argparse.ArgumentParser()
	parser.add_argument("filenames", nargs='*', type=pathlib.Path)
	parser.add_argument("--exit-zero-even-if-changed", action="store_true")
	parser.add_argument("--keep-percent-format", action="store_true")
	parser.add_argument("--keep-mock", action="store_true")
	parser.add_argument(
			"--py3-plus",
			"--py3-only",
			action="store_const",
			dest="min_version",
			default=(2, 7),
			const=(3, ),
			)
	parser.add_argument("--py36-plus", action="store_const", dest="min_version", const=(3, 6))
	parser.add_argument("--py37-plus", action="store_const", dest="min_version", const=(3, 7))
	parser.add_argument("--py38-plus", action="store_const", dest="min_version", const=(3, 8))
	parser.add_argument("--recursive", action="store_true", help="recurse subdirectories")
	args = parser.parse_args(argv)

	ret = 0

	for filename in iter_py_files(args.filenames, args.recursive):
		print(f"Checking '{filename}'")
		ret |= _fix_file(str(filename), args)

	return ret


if __name__ == "__main__":
	exit(main())
