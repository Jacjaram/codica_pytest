def test_stack():
    stack = []  # Creamos una pila vacía
    stack.append("one")  # Agregamos un elemento
    stack.append("two")  # Agregamos otro elemento

    # Verificamos que los elementos salen en orden inverso (LIFO)
    assert stack.pop() == "two"  
    assert stack.pop() == "one"