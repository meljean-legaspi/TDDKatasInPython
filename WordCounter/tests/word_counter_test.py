from word_counter import WordCounter


def test_when_input_is_one_word_return_count_for_one_word():
    assert WordCounter.count("hello") == "hello, 1"


def test_when_input_is_two_words_return_count_for_each_word():
    assert WordCounter.count("hello world") == "hello, 1\nworld, 1"


def test_when_input_has_a_word_that_repeats_return_correct_count_for_word_that_repeats():
    assert WordCounter.count('hello world hello') == "hello, 2\nworld, 1"


def test_when_input_has_comma_as_delimiter_return_count_for_words():
    assert WordCounter.count('hello,kitty') == "hello, 1\nkitty, 1"


def test_when_input_has_more_than_one_delimiter_return_count_for_words():
    assert WordCounter.count('merry christmas,kitty') == "merry, 1\nchristmas, 1\nkitty, 1"
