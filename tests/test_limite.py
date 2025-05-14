import pytest  # Necesario para manejar excepciones en pruebas

def test_pop_with_empty_stack():
    stack = []  # Pila vacía
    with pytest.raises(IndexError):  # Verificamos que pop() lanza un error
        stack.pop()