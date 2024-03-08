

def test_cicle_radius(circle):
    assert circle.radius > 0 , "circle radius not set"

def test_square_side(square):
    assert square.height > 0 , "square height not set"

def test_rect_sides(rectangle):
    assert rectangle.height > 0 and rectangle.width > 0 , "rectangle height/width not set"