from recortar import recortar

def test_cortar_texto_largo():
    assert recortar("abcdef", 4) == "abcd…"

def test_texto_corto_sin_corte():
    assert recortar("abc", 5) == "abc"



print(recortar("abcdef", 4))  # "abcd…"
print(recortar("abc", 5))     # "abc"

print(recortar("Esta es una prueba de MB para Andres Salinas", 36))