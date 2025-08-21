def recortar(texto, n):
    if len(texto) > n:
        return texto[:n] + "…"
    else:
        return texto
