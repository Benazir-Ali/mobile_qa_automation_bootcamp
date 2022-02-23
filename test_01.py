# import pytest
import logging

logging.basicConfig(filename="test_01.log")
log = logging.getLogger()


class Test01Android:
    @classmethod
    def setup_class(cls):
        log.info("This is the class level setup")

    def setup_method(self):
        log.info("This is the function level setup")

    def test_01(self):
        log.info("This is test_01 method")

    def teardown_method(self):
        log.info("This is the function level teardown")

    @classmethod
    def teardown_class(cls):
        log.info("This is the class level teardown")
