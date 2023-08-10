from Concatenation.concatenate import concatenate
import pytest

@pytest.mark.parametrize("first, second, expected_result", [('concate', 'nate', 'concatenate'),
                                                            ('', 'concatenate', 'concatenate'),
                                                            ('concatenate', '', 'concatenate'),
                                                            ('A', 'B', 'AB')])
def test_concatenate_positive(first, second, expected_result):
    assert concatenate(first, second) == expected_result


@pytest.mark.parametrize("a, b, expected_res", [('nate', 'concate', 'concatenate'),
                                                ('CONCATE', 'NATE', 'concatenate'),
                                                ('  concate  ', '  nate  ', 'concatenate')])
def test_concatenate_not_equal(a, b, expected_res):
    assert concatenate(a, b) != expected_res







