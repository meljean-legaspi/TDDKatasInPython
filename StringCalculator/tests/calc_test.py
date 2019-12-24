from calc import StringCalculator


def test_when_input_is_empty_string_return_zero():
    assert StringCalculator.add("") == 0


def test_when_input_is_one_number_return_number():
    assert StringCalculator.add("1") == 1


def test_when_input_has_two_numbers_return_sum():
    assert StringCalculator.add("1,2") == 3


def test_when_input_has_five_numbers_return_sum():
    assert StringCalculator.add("1,2,3,4,5") == 15


def test_when_input_has_newline_return_sum():
    assert StringCalculator.add("1\n2,3") == 6


def test_when_input_has_different_delimiter_return_sum():
    assert StringCalculator.add("//;\n1;2;3") == 6
