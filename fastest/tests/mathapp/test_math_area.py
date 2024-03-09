import pytest

def test_cicle_radius(circle):
    assert circle.radius > 0 , "circle radius not set"

def test_square_side(square):
    assert square.height > 0 , "square height not set"

def test_rect_sides(rectangle):
    assert rectangle.height > 0 and rectangle.width > 0 , "rectangle height/width not set"

def test_square_area(square):
    square.calculate_and_set_area()
    assert square.area == square.height * square.height

@pytest.mark.parametrize("height,width", [(10,10), (10,5), (5,5)])
def test_rectangle_with_param(rectangle, height, width):
    rectangle.height = height
    rectangle.width = width
    rectangle.calculate_and_set_area()
    assert rectangle.area == height * width

def test_circle_fixture_param(circle_fixture_param):
    circle_fixture_param.calculate_and_set_area()
    assert circle_fixture_param.area > 0

def test_circle_area(circle_with_area):
    c, a, p = circle_with_area
    c.calculate_and_set_area()
    c.calculate_and_set_perimeter()
    assert c.area == a and c.perimeter == p

