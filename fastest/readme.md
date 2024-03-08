## sitaram abhyas with pytest

### pytest framework
- make it easy to write small/readable tests that can be scaled

### pytest discoveries
- pytest start with `testpaths` if configured else with current dir
- pytest collect files `test_*.py/*_test.py` from dir/subdir
- pytest collect tests from these collected files with `test` prefix functions.
- pytest collect tests methods prefixed with `test_` from class prefixed `Test` without `__init__`.
- methods decorated with `@staticmethod` and `@classmethod` also considered test functions.

### pytest running ways

run test in a module or list of modules
`pytest test_mod.py`
`pytest test_mod_one.py test_mod_two.py`

run test with dir
`pytest testing/ testing2/`

run tests by keyword expressions
`pytest -k 'MyClass and not method'`

run tests by collect argument: specific test within a module
`pytest tests/test_mod.py::test_func`

run tests by collect argument: all tests in a class
`pytest tests/test_mod.py::TestClass`

run tests by collect argument: specific test method
`pytest tests/test_mod.py::TestClass::test_method`

run tests by collect argument: specific parametrization of a test
`pytest tests/test_mod.py::test_func[x1,y2]`

run tests by collect argument: tests by marker expressions
`pytest -m slow`

run tests by collect argument:  tests from packages
`pytest --pyargs pkg.testing`


### pytest marker @pytest.mark
- `pytest.mark` used to apply meta data to test functions only


### pytest fixture @pytest.fixture
- fixture provide a defined, reliable and consistent context for the tests.
- fixture provide a fixed baseline upon which tests can reliably and repeatedly execute, enhancing test isolation and reproducibility.
- fixture used for setting up and tearing down test environments.
- fixture defines the steps and data that consitute the *arrange* phase of a test.
- fixtures are requested by test functions or other fixtures by declaring them as argument.
- fixture are available for tests to request if they are in the scope.
- why scope is needed ?
- fixture requiring network access, database access are time-expensive to create.
- so destroying such fixture with each test is not optimal.

- **function**: the default scope, the fixture is destroyed at the end of the test.
- **class**: the fixture is destroyed during teardown of the last test in the class.
- **module**: the fixture is destroyed during teardown of the last test in the module.
- **package**: the fixture is destroyed during teardown of the last test in the package.
- **session**: the fixture is destroyed at the end of the test session.


### pytest conftest.py(plugin)
- conftest.py: sharing fixtures across multiple files
- fixture/hooks defined with root conftest will be available to subdir tests.
- fixture/hooks defined in subdir conftest will not be available to root tests.



### pytest hooks @pytest.hookimpl
- hooks are used to modify/extend default bevaiour of framework.
- hooks are gateway to framework where you can plugin/alter default.
- various stages hooks allow to inject code at different stage of testing.
- bootstrapping -> initialization -> collection -> runtest -> reporting -> debugging
- bootstrapping : called at begin and end of testing.
- bootstrapping : crucial for setting up/tear down configuration/env that needed for testing.

- initialization: these hooks come into play after bootstrap.
- initialization: instrumental for tasks like adding command-line-option or adding new plugings.
- initialization: these hooks set stage for customized testing env.

- collection    : deals with discovering and collecting tests.
- collection    : they give power to collecting strategy allow to add/modify/skip tests on custom criteria.

- runtest       : these hooks offer way to customize test execution.
- runtest       : hooks enables action before/during/after a test in run.
- runtest       : actions can be from setting up test data to cleaning resource after a test.

- reporting     : these hooks are all about how test results are processed/presented.
- reporting     : way to customoze the output/create custom reports

- debugging     : these hooks are valuable for debugging.
- debugging     : comes into play a when tests fail or when you need to drop into an interactive session.
- debugging     : they can help in inspecting the state of a test at various points or managing breakpoints.



