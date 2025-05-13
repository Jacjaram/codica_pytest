from codica_pytest.example import reverse

def test_reverse():
    assert reverse('Códica') == 'acídoC'

def test_reverse_for_empty_string():
    assert reverse('') == ''