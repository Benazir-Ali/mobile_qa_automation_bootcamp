import pytest
import logging

logging.basicConfig(filename="test_02.log")
log = logging.getLogger()


class Test02Android:
    @pytest.mark.xfail(reason="Unable to execute test")
    def test_02(self):
        log.info("This test is expected to fail")
