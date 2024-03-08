## sitaram abhyas with pytest

### pytest framework
- make it easy to write small/readable tests that can be scaled

### pytest discoveries
- pytest start with `testpaths` if configured else with current dir
- pytest collect files `test_*.py/*_test.py` from dir/subdir
- pytest collect tests from these collected files with `test` prefix functions.
- pytest collect tests methods prefixed with `test_` from class prefixed `Test` without `__init__`.
- methods decorated with `@staticmethod` and `@classmethod` also considered test functions.

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
> A fixture is only available for tests to request if they are in the scope that fixture is defined in scope.
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

> Fixtures requiring network access depend on connectivity and are usually time-expensive to create.
> Extending the previous example, we can add a scope="module" parameter to the @pytest.fixture invocation to cause a smtp_connection fixture function,
> responsible to create a connection to a preexisting SMTP server, to only be invoked once per test module (the default is to invoke once per test function).
> Multiple test functions in a test module will thus each receive the same smtp_connection fixture instance, thus saving time.
> Possible values for scope are: function, class, module, package or session.

### Pytest Hooks

> `pytest_configure` is used to add/modify global config object.
> any change to config in `pytest_configure` hook will be reflected to global.
> global config can be access in test/fixture using `request.config` or `pytestconfig` fixture.
> `pytest_configure` is used to add/modify global config, session-wide settings, or variables
> that remain constants during session.

> `pytest_addoption` is used to add custom option from command line.
> either your can use this hook or can add option in `pytest.ini` file.
> but if your custom option has variable values, better use command line.

