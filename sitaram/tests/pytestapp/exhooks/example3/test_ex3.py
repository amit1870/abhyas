def test_pytest_addoption(request):
    # get option added with parser addoption
    global_path = request.config.getoption("global_path")
    print(global_path)

    assert True

def test_pytest_with_fixture(pytestconfig):
    print(pytestconfig.option)
    assert pytestconfig.global_path == "/home/guruvar/amit"
