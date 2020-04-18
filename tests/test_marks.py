import sys

import pytest


class TestMarks(object):
    @pytest.mark.skip(reason="not implementation")
    def test_the_unknown(self):
        """
        跳过不执行，因为被测逻辑还没有被实现
        """
        assert 0

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
    def test_skipif(self):
        """
        低于python3.7版本不执行这条测试用例
        :return:
        """
        assert 1

    @pytest.mark.xfail
    def test_xfail(self):
        """
        Indicate that you expect it to fail
        这条用例失败时，测试结果被标记为xfail（expected to fail），并且不打印错误信息。
        这条用例执行成功时，测试结果被标记为xpassed（unexpectedly passing）
        """
        assert 0

    @pytest.mark.xfail(run=False)
    def test_xfail_not_run(self):
        """
        run=False表示这条用例不用执行
        """
        assert 0

    @pytest.mark.slow
    def test_slow(self):
        """
        自定义标签
        """
        assert 0

