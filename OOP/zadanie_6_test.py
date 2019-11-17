from zadanie_6 import Vector

def test_add_vector():
    v1 = Vector(1, 3)
    v2 = Vector(2, 4)

    result = v1 + v2
    assert result.x == 3
    assert result.y == 7

def test_sub_vector():
    v1 = Vector(1, 3)
    v2 = Vector(2, 4)

    result = v1 - v2
    assert result.x == -1
    assert result.y == -1

def test_mul_by_int():
    v = Vector(2, 3)
    result = v * 5
    assert result.x == 10
    assert result.y == 15
    result = 5 * v
    assert result.x == 10
    assert result.y == 15

def test_mul_by_other_vector():
    v1 = Vector(2, 3)
    v2 = Vector(3, 2)
    result = v1 * v2
    assert result == 12

def test_vector_comparasion():
    v1 = Vector(1, 1)
    v2 = Vector(4, 4)

    assert v2 > v1

def test_vector_string():
    v = Vector(1, 1)
    assert str(v) == "Vector (x = 1, y = 1)"
