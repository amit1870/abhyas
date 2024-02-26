def pytest_configure(config):
    config.addinivalue_line("markers" , "ui: mark test as a UI test")
    config.addinivalue_line("markers" , "api: mark test as a API test")

