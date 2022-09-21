# stdlib
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

# 3rd party
from domdf_python_tools.paths import PathPlus, in_directory

# this package
import pyupgrade_directories
import pyupgrade_directories.__main__


@contextmanager
def fail_on_systemexit() -> Iterator[None]:
	try:
		yield
	except SystemExit as e:
		raise ValueError(f"Process exited with code {e.code}")


def test_iter_py_files(tmp_pathplus: PathPlus):
	(tmp_pathplus / "code.py").write_text("print('Hello World')\n")
	(tmp_pathplus / "code.pyi").write_text("def foo(): ...\n")
	(tmp_pathplus / "code.pyd").touch()
	(tmp_pathplus / "code.pyc").touch()
	(tmp_pathplus / "code.pyo").touch()
	(tmp_pathplus / "README.txt").write_text("This is the readme")

	(tmp_pathplus / "package").mkdir()
	(tmp_pathplus / "package" / "submodule.py").write_text("print('A submodule')\n")

	(tmp_pathplus / "venv" / "lib" / "python3.6" / "site-packages").mkdir(parents=True)
	(tmp_pathplus / "venv" / "lib" / "python3.6" / "site-packages"
		/ "installed.py").write_text("print('An installed module')\n")

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert list(
				pyupgrade_directories.iter_py_files([Path("code.py"), Path("README.txt"), Path("i.dont.exist")])
				) == [tmp_pathplus / "code.py"]

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert sorted(pyupgrade_directories.iter_py_files([tmp_pathplus])) == [
				tmp_pathplus / "code.py",
				tmp_pathplus / "code.pyi",
		]

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert sorted(pyupgrade_directories.iter_py_files([tmp_pathplus], recursive=True)) == [
			tmp_pathplus / "code.py",
			tmp_pathplus / "code.pyi",
			tmp_pathplus / "package/submodule.py",
		]


def test_main(tmp_pathplus: PathPlus):
	(tmp_pathplus / "code.py").write_text("print('Hello World')\n")
	(tmp_pathplus / "code.pyi").write_text("def foo(): ...\n")
	(tmp_pathplus / "code.pyd").touch()
	(tmp_pathplus / "code.pyc").touch()
	(tmp_pathplus / "code.pyo").touch()
	(tmp_pathplus / "README.txt").write_text("This is the readme")

	(tmp_pathplus / "package").mkdir()
	(tmp_pathplus / "submodule.py").write_text("print('A submodule')\n")

	(tmp_pathplus / "venv" / "lib" / "python3.6" / "site-packages").mkdir(parents=True)
	(tmp_pathplus / "venv" / "lib" / "python3.6" / "site-packages"
		/ "installed.py").write_text("print('An installed module')\n")

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert pyupgrade_directories.__main__.main(["code.py", "README.txt", "i.dont.exist"]) == 0

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert pyupgrade_directories.__main__.main([tmp_pathplus.as_posix()]) == 0

	with in_directory(tmp_pathplus), fail_on_systemexit():
		assert pyupgrade_directories.__main__.main([tmp_pathplus.as_posix(), "--recursive"]) == 0

	assert (tmp_pathplus / "code.py").read_text() == "print('Hello World')\n"
	assert (tmp_pathplus / "code.pyi").read_text() == "def foo(): ...\n"
	assert (tmp_pathplus / "README.txt").read_text() == "This is the readme"
	assert (tmp_pathplus / "submodule.py").read_text() == "print('A submodule')\n"
