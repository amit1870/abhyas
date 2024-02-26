import pytest

def test_global_path(request):
    global_root = request.config.global_root
    print("global path :", global_root)
    assert True
