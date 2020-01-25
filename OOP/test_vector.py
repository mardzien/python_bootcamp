from vector import Vector


def test_add_vectors():
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)

    result = v1 + v2
    assert result.x == 5
    assert result.y == 10


def test_sub_vectors():
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)

    result = v1 - v2
    assert result.x == -3
    assert result.y == -4


def test_mul_by_integer():
    v = Vector(2, 3)
    result = v * 5
    assert result.x == 10
    assert result.y == 15
    result = 5 * v
    assert result.x == 10
    assert result.y == 15


def test_mul_by_other_vector():
    "monżenie skalarne: v1 = a1, b1, v2=a2, b2  v1*v2 = a1*a2 + b1*b2"
    v1 = Vector(2, 3)
    v2 = Vector(3, 2)
    result = v1 * v2
    assert result == 12


def test_vector_comparison():
    v1 = Vector(1, 1)
    v2 = Vector(4, 4)

    assert v2 > v1


def test_vector_str():
    v1 = Vector(1, 1)
    assert str(v1) == "Vector(x=1, y=1)"
