import pytest

@pytest.mark.ui
def test_ui_componet():
    print("testing ui component")
    assert True

@pytest.mark.api
def test_api_call():
    print("testing api call")
