from mathematica.geometry.figures import square_arena, triangle_arena



def test_square_area():
    assert square_arena(4) == 16

def test_triangle_area():
    assert triangle_area(4, 2) == 4.0