#  This file is managed by `git_helper`. Don't edit it directly
#  Copyright (C) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This file is distributed under the same license terms as the program it came with.
#  There will probably be a file called LICEN[S/C]E in the same directory as this file.
#
#  In any case, this program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py
#

# stdlib
import pathlib

__all__ = [
		"__copyright__",
		"__version__",
		"modname",
		"pypi_name",
		"py_modules",
		"entry_points",
		"__license__",
		"short_desc",
		"author",
		"author_email",
		"github_username",
		"web",
		"github_url",
		"project_urls",
		"repo_root",
		"long_description",
		"install_requires",
		"extras_require",
		"classifiers",
		"keywords",
		"import_name",
		]

__copyright__ = """
2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

__version__ = "0.0.3"

modname = "pyupgrade-directories"
pypi_name = "pyupgrade-directories"
import_name = "pyupgrade_directories"
py_modules = []
entry_points = {
		"console_scripts": ['pyup-dirs=pyupgrade_directories.__main__:main', 'pyup_dirs=pyupgrade_directories.__main__:main']
		}

__license__ = "MIT"

short_desc = "Run pyupgrade on all files in a directory, and optionally recursively."

__author__ = author = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
github_username = "domdfcoding"
web = github_url = f"https://github.com/domdfcoding/pyupgrade-directories"
project_urls = {
		"Documentation": f"https://pyupgrade-directories.readthedocs.io",
		"Issue Tracker": f"{github_url}/issues",
		"Source Code": github_url,
		}

repo_root = pathlib.Path(__file__).parent

# Get info from files; set: long_description
long_description = (repo_root / "README.rst").read_text().replace("0.0.3", __version__) + '\n'

install_requires = (repo_root / "requirements.txt").read_text().split('\n')
extras_require = {'all': []}

classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Utilities',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Programming Language :: Python :: 3 :: Only',
		'Typing :: Typed',

		]

keywords = ""
