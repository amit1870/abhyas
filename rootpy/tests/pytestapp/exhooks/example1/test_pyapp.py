import pytest

@pytest.mark.ui
def test_ui_component():
    print("guruvarsitaram : this is ui test")
    assert True

@pytest.mark.api
def test_api_call():
    print("guruvarsitaram : this is API test")
    assert True

