# Pytest Concept Abhyas

## Pytest

> pytest framework makes it easy to write small, readable tests and can scale to support
> complex functional testing for applications and libraries.

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




## Fixtures
> in testing , a fixture provides a defined, reliable and consistent context for the tests.
> fixture can include enviroment context or content such as dataset.
> Fixture define the steps and data that consitute the `arrange` phase of a test.
> in pytest, fixtures are functions that serve this purpose.
> we can tell pytest that a particular function is a fixture by decorating it with `@pytest.fixture`.
> Fixtures are requested by test functions or other fixtures by declaring them as argument names.
> Tests don't have to be limited to a single fixture, either.
> They can depend on as many fixtures as you want, and fixtures can use other fixtures, as well.
> This is where pytest’s fixture system really shines.


> Fixture availability is determined from the perspective of the test.
> A fixture is only available for tests to request if they are in the scope that fixture is defined in.s
> If a fixture is defined inside a class, it can only be requested by tests inside that class.
> if a fixture is defined inside the global scope of the module, then every test in that module, even if it’s defined inside a class, can request it.

> Autouse fixtures are executed first within their scope.
> Autouse fixtures are assumed to apply to every test that could reference them, so they are executed before other fixtures in that scope. 
> Fixtures that are requested by autouse fixtures effectively become autouse fixtures themselves for the tests.
> So if fixture a is autouse and fixture b is not, but fixture a requests fixture b, then fixture b will effectively be an autouse fixture as well, but only for the tests that a applies to.

> conftest.py: sharing fixtures across multiple files
> 


### Fixture scopes
> Fixtures are created when first requested by a test, and are destroyed based on their scope:

> `function`: the default scope, the fixture is destroyed at the end of the test.

> `class`: the fixture is destroyed during teardown of the last test in the class.

> `module`: the fixture is destroyed during teardown of the last test in the module.

> `package`: the fixture is destroyed during teardown of the last test in the package.

> `session`: the fixture is destroyed at the end of the test session.