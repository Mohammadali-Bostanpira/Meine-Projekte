from plates import is_valid



def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB123") == True



def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False



def test_start_letters():
    assert not is_valid("1ABC")
    assert not is_valid("A2BC")


def test_numbers_position():
    assert not is_valid("CS05")
    assert not is_valid("CS50P")
    assert not is_valid("22")


def test_no_punctuation():
    assert not is_valid("CS!0")
    assert not is_valid("CS-50")
    assert not is_valid("AB 12")


def test_alphanumeric_only():
    assert not is_valid("AB01")
    assert not is_valid("PI3.14")



