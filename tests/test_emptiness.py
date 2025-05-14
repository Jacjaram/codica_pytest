def test_emptiness():
    stack = []  # Creamos una pila vacía
    assert not stack  # La pila debería estar vacía
    stack.append("one")  # Agregamos un elemento
    assert bool(stack)  # Ahora debería estar llena
    stack.pop()  # Quitamos el único elemento
    assert not stack  # Después de eliminar el elemento, debe estar vacía de nuevo
