import pytest

@pytest.hookimpl()
def pytest_cmdline_main(config):
    print('pytest_cmdline_main hook', config)
    print(config.option)

@pytest.hookimpl()
def pytest_runtest_setup(item):
    print('pytest_runtest_setup hook', item)

@pytest.hookimpl()
def pytest_configure(config):
    config.addinivalue_line("markers", "exfixture: use this marker for fixture examples")

@pytest.fixture(scope="function", autouse=False)
def fixture_scope_function():
    print("fixture with scope function entered...")
    yield ['amit','sachin','sunil','shivkumar','rajkumar','rajesh']
    print("fixture with scope function finshed.")

@pytest.fixture(scope="class", autouse=False)
def fixture_scope_class():
    print("fixture with scope class entered...")
    yield ['class-amit','class-sachin','class-sunil','class-shivkumar','class-rajkumar','class-rajesh']
    print("fixture with scope class finshed.")

@pytest.fixture(scope="module", autouse=False)
def fixture_scope_module():
    print("fixture with scope module entered...")
    yield ['module-amit','module-sachin','module-sunil','module-shivkumar','module-rajkumar','module-rajesh']
    print("fixture with scope module finshed.")

@pytest.fixture(scope="package", autouse=False)
def fixture_scope_package():
    print("fixture with scope package entered...")
    yield ['package-amit','package-sachin','package-sunil','package-shivkumar','package-rajkumar','package-rajesh']
    print("fixture with scope package finshed.")

@pytest.fixture(scope="session", autouse=False)
def fixture_scope_session():
    print("fixture with scope session entered...")
    yield ['session-amit','session-sachin','session-sunil','session-shivkumar','session-rajkumar','session-rajesh']
    print("fixture with scope session finshed.")