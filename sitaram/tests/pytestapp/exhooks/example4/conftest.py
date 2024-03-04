import pytest

@pytest.hookimpl()
def pytest_sessionstart(session):
    print("guruvar sitaram from `pytest_sessionstart` hook")

@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    print("guruvar sitaram from `pyest_sessionfinish` hook")
    print("session finshes with exitstatus ", exitstatus)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):

    if call.when == "call":
        outcome = call.excinfo

        try:
            test_outcome = "guruvar" if outcome else "sitaram"
            test_duration = call.duration
            test_item = item.nodeid

            print(f"test {test_item} with outcome {test_outcome} with duration {test_duration}")
        except Exception as e:
            print(f"sitaram {e}")
