import pytest
import logging

logging.basicConfig(filename="test_01.log", level=logging.DEBUG)
log = logging.getLogger()


class Test02Android:
    @pytest.mark.xfail(reason="Unable to execute test")
    def test_02(self):
        log.info("This test is expected to fail")

