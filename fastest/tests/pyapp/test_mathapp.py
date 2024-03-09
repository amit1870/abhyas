import pytest

@pytest.mark.xfail
def test_circle_radius(circle_gbl):
    assert circle_gbl.radius > 0 , "circle radius not set"