def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default")
    parser.addoption("--summary", default=True)

def pytest_configure(config):
    config.custom_option = config.getoption("--custom-option")
    config.summary = config.getoption("--summary")
    config.non_summary = False
    config.capture = "no"


