import re

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "cli: mark a test for cli password"
    )
    config.password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&-])[A-Za-z\d@$!%*?&-]{8,}$')


