import pytest

@pytest.mark.hook_config
def test_added_param(pytestconfig):
    assert pytestconfig.global_path == '/home/guruvar/amit'

@pytest.mark.xfail
def test_missing_param(pytestconfig):
    print(pytestconfig.option)
    assert pytestconfig.missing == '/home/guruvar/amit'

@pytest.mark.xfail
def test_added_param_with(request):
    assert request.config.global_path == '/home/guruvar/amit'
