# Pytest Concept Abhyas

## Pytest

> pytest framework makes it easy to write small, readable tests and can scale to support
> complex functionaly testing for applications and libraries.

## Python test discoveries

> pytest will start with testpaths if configured, else with current dir.
> pytest will collect file `test_*.py` or `*_test.py` from these dirs until all sub dirs files included.
> then pytest will collect test from these collected files with `test` prefix functions.
> and `test` prefixed functions or methods from class prefixed `Test` without `__init__`
> methods decorated with `@staticmethod` and `@classmethod` also considered.

## How to pytest

> Run tests in a module
> `pytest test_mod.py`

> Run tests in a directory
> `pytest testing/ testing2/`

> Run tests by keyword expressions
> `pytest -k 'MyClass and not method'`

> Run tests by collection arguments

> To run a specific test within a module:
> `pytest tests/test_mod.py::test_func`

> To run all tests in a class:
> `pytest tests/test_mod.py::TestClass`

> Specifying a specific test method:
> `pytest tests/test_mod.py::TestClass::test_method`

> Specifying a specific parametrization of a test:
> `pytest tests/test_mod.py::test_func[x1,y2]`

> Run tests by marker expressions
> `pytest -m slow`

> Run tests from packages
> `pytest --pyargs pkg.testing`



## Managing loading of plugins

> Early loading plugins
> `pytest -p mypluginmodule`

> Disabling plugins
> `pytest -p no:doctest`

> 


## Pytest Mark

> Marks `pytest.mark` can be used apply meta data to test functions (but not fixtures), which can then be accessed by fixtures or plugins.
> 

## Add more on importlib

