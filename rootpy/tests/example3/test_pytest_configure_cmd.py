def test_custom_option(pytestconfig):
    assert pytestconfig.custom_option == "default"

def test_summary(pytestconfig):
    assert pytestconfig.summary == True

def test_change_quiet(pytestconfig):
    print("silent the output of test")
    assert True
