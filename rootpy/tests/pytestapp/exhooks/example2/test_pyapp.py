def test_config_add(request):
    # print all config values with request.config.option
    print(request.config.option)

    # get option added dynamically in pytest_configure
    global_path = request.config.global_path
    print(global_path)

    # get option added dynamically with request.config.option
    # if tried to get option added dynamically will error
    # to add option with parser addoption in pytest_addoption hook
    # and you can access with below syntax
    # global_path = request.config.getoption("global_path")
    # print(global_path)


    # get option from global config object
    importmode = request.config.getoption('importmode')
    print(importmode)

    assert True

