import logging
import os

import pytest
import self as self
from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator

@pytest.mark.non_browser
class TestTc07FailedDivideByZero(DriverManager, ReportGenerator):

    def test_failed_divide_by_zero(self):
        ReportGenerator.setTestCaseDescription(self, "Verify Defect creation")
        try:
            i = 1/0
            print(i)
        except Exception as ex:
            ReportGenerator.captureErrorInfo(self, "")
            logging.error(f"Exception: {ex}")
