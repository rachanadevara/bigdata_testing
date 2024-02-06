import pytest
from assertpy import assert_that
from reusables.DataTesting import DataTesting
from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator

@pytest.mark.non_browser
class TestTc08DataComparisonUsingCSV(DriverManager, ReportGenerator):
    def test_datacomparisoncsv(self):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")
        status=DataTesting.csvcomparison(self,self.framework_path+"/tests/resources/inputs/emp.csv", self.framework_path+"/tests/resources/inputs/emp1.csv",[],"CSV","CSV")
        assert_that(status).is_false()
