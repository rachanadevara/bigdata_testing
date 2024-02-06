from pathlib import Path

import pytest
import self as self

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator
from tests.autoIt.Notepad import Notepad

"""/************************************************************************************************************************
* Name of the Class   : TestTc04AutoitIntegration
* Description  : This class is used to validate the framework capability of AutoIt Integration
*************************************************************************************************************************/"""

@pytest.mark.non_browser
class TestTc04AutoitIntegration(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_Autoit()
    * Description  : Test method for uploading a file in the application
    ******************************************************************************************************************/"""

    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "frameworksanity", {"AddText"}))
    def test_Autoit(self,excel_data):
        ReportGenerator.setTestCaseDescription(self, "Verify AutoIT")

        Notepad.open_Notepad(self)

        Notepad.edit_Notepad(self, excel_data.get("AddText"))

        ReportGenerator.captureTestEvidence(self, "Verify Notepad",
                                            "Hello world is displayed",
                                            "Hello world was displayed",
                                            "windows")

        Notepad.save_and_close_Notepad(self)
