def pytest_addoption(parser):
    parser.addoption("--global-path" , action="store", default="/home/guruvar/amit")

def pytest_configure(config):
    config.global_path = config.getoption("--global-path")

