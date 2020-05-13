import pytest


class TestStringAssertions(object):
    def test_string_1(self):
        assert "spam" == "eggs"

    def test_string_2(self):
        assert "foo 1 bar" == "foo 2 bar"

    def test_string_3(self):
        assert "foo\nspam\nbar" == "foo\neggs\nbar"

    def test_string_4(self):
        def f():
            return "streaming"

        assert f().startswith('S')


def test_function():
    def f():
        return [1, 2, 3]

    assert f() == [1, 2, 4]


class TestCollections(object):
    def test_dict(self):
        assert {"a": 0, "b": 1, "c": 0} == {"a": 0, "b": 2, "d": 0}

    def test_dict2(self):
        exp = {"a": 0, "b": {"c": 0}}
        act = {"a": 0, "b": {"c": 2}}
        assert exp == act

    def test_list(self):
        left_list = [0, 1, 2]
        right_list = [0, 1, 3]
        assert left_list == right_list, "jjjjjjj"

    def test_list2(self):
        assert [0, 1, 2] == [0, 1, [1, 2]]

    def test_list3(self):
        assert 2 in [0, 1, [1, 2]]

    def test_set(self):
        assert {0, 10, 11, 12} == {0, 20, 21}


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0
    assert 'division by zero' in str(excinfo.value)
