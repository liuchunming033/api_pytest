import pytest
import requests

from utils.commlib import get_test_data

cases, list_params = get_test_data("/Users/chunming.liu/learn/api_pytest/data/test_in_theaters.yaml")


class TestInTheaters(object):
    @pytest.fixture(scope="class")
    def preparation(self):
        print("在数据库中准备测试数据")
        test_data = "在数据库中准备测试数据"
        yield test_data
        print("清理测试数据")

    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, env, case, http, expected, preparation):
        r = requests.request(http["method"],
                             url=env["host"]["douban"] + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        assert response["count"] == expected['response']["count"]
        assert response["start"] == expected['response']["start"]
        assert response["title"] == expected['response']["title"], "实际的标题是：{}".format(response["title"])
