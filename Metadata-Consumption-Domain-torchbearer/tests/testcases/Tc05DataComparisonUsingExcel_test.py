import pytest
import self as self

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator
from reusables.TestDataManager import TestDataManager

"""/************************************************************************************************************************
* Name of the Class   : TestTc05DataComparisonUsingExcel
* Description  : This class is used to validate the framework capability of data comparison using Excel
*************************************************************************************************************************/"""

@pytest.mark.non_browser
@pytest.mark.frameworkSanity
class TestTc05DataComparisonUsingExcel(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_datacomarision()
    * Description  : Test method to validate positive and negative scenario of excel comparison
    ******************************************************************************************************************/"""

    def test_datacomparison(self):
        ReportGenerator.setTestCaseDescription(self, "Verify Excel comparison")
        list1 = [('one', 'two'), ('three', 'four')]
        list2 = [('one', 'two'), ('three', 'five')]
        is_data_same = TestDataManager.dataComparisionListlist(self, list1, list2, 'sheet1', 'listcomparision')
        if is_data_same:
            self.captureTestEvidence(
                "Verify Excel comparison for two lists : " ,
                "Data should be matched",
                "Data matched, please refer attached excel sheet : listcomparision.xlsx" ,
                "null")
        else:

            self.captureTestEvidence(
                "Verify Excel comparison for : " ,
                "Data should be matched",
                "Data did not matched, please refer attached excel sheet : listcomparision.xlsx" ,
                "null")

