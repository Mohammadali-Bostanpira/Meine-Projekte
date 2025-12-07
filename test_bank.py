from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello babe") == 0


def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("Hallo") == 20



def test_else():
    assert value("you") == 100
    assert value("good") == 100
    assert value("bye") == 100
