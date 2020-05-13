import inspect
import os
import re

import allure
import pytest
import yaml
import logging
from _pytest.assertion.util import assertrepr_compare


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")


@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


def pytest_assertrepr_compare(config, op, left, right):
    left_name, right_name = inspect.stack()[7].code_context[0].lstrip().lstrip('assert').rstrip('\n').split(op)
    pytest_output = assertrepr_compare(config, op, left, right)
    logging.debug("{0} is\n {1}".format(left_name, left))
    logging.debug("{0} is\n {1}".format(right_name, right))
    with allure.step("校验结果"):
        allure.attach(str(left), left_name)
        allure.attach(str(right), right_name)
    return pytest_output
