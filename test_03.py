import pytest
import logging

logging.basicConfig(filename="test_03.log", level=logging.DEBUG)
log = logging.getLogger()


class Test03Android:
    @pytest.mark.skip(reason="Unable to execute test")
    def test_03(self):
        log.info("This test is to be skipped")
