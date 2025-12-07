from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("voroodi") == "vrd"
    assert shorten("mohammad") == "mhmmd"
    assert shorten("What") == "Wht"
    assert shorten("ghOm") == "ghm"
    assert shorten("CS50") == "CS50"
    assert shorten("boy,girl") == "by,grl"
