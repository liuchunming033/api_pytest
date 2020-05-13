# content of utils/assertions.py


def assertion(exp, act):
    assert exp == act, "Expectation is {} ,but actual result is {}".format(exp, act)
