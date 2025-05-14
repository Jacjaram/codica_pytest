from codica_pytest.example import reverse

def test_reverse():
    assert reverse('Códica') == 'acidóC'

def test_reverse_for_empty_string():
    assert reverse('') == ''