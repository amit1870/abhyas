import pytest

def test_password_generator(get_strong_password, pytestconfig):
    # print(pytestconfig.option) # will include config added from cmd
    password = get_strong_password
    assert pytestconfig.password_pattern.match(password), "password does not match specs"

@pytest.mark.cli
def test_password_cli(request):
    # print(request.config.option) # will include config added from cmd
    password = request.config.getoption("--password")
    assert request.config.password_pattern.match(password), "password does not match specs"


@pytest.mark.xfail(reason="simple password should not pass check")
def test_password_simple(get_simple_password, pytestconfig):
    password = get_simple_password
    assert pytestconfig.password_pattern.match(password), "password does not match specs"

@pytest.mark.xfail(reason="strong password should pass check")
def test_password_strong(pytestconfig):
    password = '4BG%GSF98#$jdh'
    assert pytestconfig.password_pattern.match(password), "password does not match specs"


@pytest.mark.parametrize("get_param_password", ['h#hd%hjsj', 'simEw@123'], indirect=True)
def test_param_password(get_param_password, pytestconfig):
    password = get_param_password
    assert pytestconfig.password_pattern.match(password), "password does not match specs"
