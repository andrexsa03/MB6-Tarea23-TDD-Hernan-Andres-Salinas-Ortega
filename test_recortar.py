from recortar import recortar

def test_cortar_texto_largo():
    assert recortar("abcdef", 4) == "abcd…"

def test_texto_corto_sin_corte():
    assert recortar("abc", 5) == "abc"



