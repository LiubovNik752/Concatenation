from Concatenation.concatenate import concatenate
import pytest

@pytest.mark.parametrize("first, second, expected_result", [('concate', 'nate', 'concatenate'),
                                                            ('', 'concatenate', 'concatenate'),
                                                            ('concatenate', '', 'concatenate'),
                                                            ('A', 'B', 'AB')])
def test_concatenate_positive(first, second, expected_result):
    assert concatenate(first, second) == expected_result


@pytest.mark.parametrize("a, b, expected_res", [('nate', 'concate', 'concatenate'),
                                                ('Concate', 'nate', 'concatenate'),
                                                (1, 2, 12)])
def test_concatenate_not_equal(a, b, expected_res):
    assert concatenate(a, b) != expected_res


@pytest.mark.parametrize("expected_exception, c, d", [(TypeError, "1", 2),
                                                      (TypeError, "name", ['surename'])])
def test_concatenate_with_error(expected_exception, c, d):
    with pytest.raises(expected_exception):
        concatenate(c, d)





