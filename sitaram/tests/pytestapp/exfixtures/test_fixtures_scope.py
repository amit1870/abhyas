import pytest

@pytest.mark.exfixture
def test_fixture_scope_function_one(fixture_scope_function):
    assert 'amit' in fixture_scope_function

@pytest.mark.exfixture
def test_fixture_scope_function_two(fixture_scope_function):
    assert 'sachin' in fixture_scope_function

@pytest.mark.exfixture
def test_fixture_scope_class_one(fixture_scope_class):
    assert 'class-amit' in fixture_scope_class

@pytest.mark.exfixture
def test_fixture_scope_class_two(fixture_scope_class):
    assert 'class-sachin' in fixture_scope_class

@pytest.mark.exfixture
def test_fixture_scope_module_one(fixture_scope_module):
    assert 'module-sachin' in fixture_scope_module

@pytest.mark.exfixture
def test_fixture_scope_module_two(fixture_scope_module):
    assert 'module-sachin' in fixture_scope_module

@pytest.mark.exfixture
def test_fixture_scope_module_three(fixture_scope_module):
    assert 'module-sachin' in fixture_scope_module

@pytest.mark.exfixture
def test_fixture_scope_package_one(fixture_scope_package):
    assert 'package-sachin' in fixture_scope_package

@pytest.mark.exfixture
def test_fixture_scope_package_two(fixture_scope_package):
    assert 'package-sachin' in fixture_scope_package

@pytest.mark.exfixture
def test_fixture_scope_session_one(fixture_scope_session):
    assert 'session-sachin' in fixture_scope_session

@pytest.mark.exfixture
def test_fixture_scope_session_two(fixture_scope_session):
    assert 'session-sachin' in fixture_scope_session
