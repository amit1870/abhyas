def pytest_addoption(parser):
    parser.addoption("--global-path", action="store", default="/home/guruvar/amit")

def pytest_configure(config):
    config.addinivalue_line("markers", "hook_config: add this test to hook config")
    config.addinivalue_line("markers", "hook_conf: add this test to hook config")
    config.global_path = config.getoption("--global-path")
