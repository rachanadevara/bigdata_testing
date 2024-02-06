
from pathlib import Path

import pytest

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator
from reusables.WebCommonMethods import WebCommonMethods
from tests.mylearning.MyLearningLogin import MyLearningLogin

import self as self

from tests.mylearning.WebLocatorLibrary import WebLocatorLibrary

"""/************************************************************************************************************************
* Name of the Class   : TestTc01VerifyNavigationOfWebApplication
* Description  : This class is used to validate the framework capability to verify Login for multiple data
*************************************************************************************************************************/"""
@pytest.mark.frameworkSanity
class TestTc01VerifyNavigationOfWebApplication(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_web_application()
    * Description  : Verify web application login
    ******************************************************************************************************************/"""

    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "frameworksanity", {"UserName", "Password"}))

    def test_web_application(self, excel_data):

        ReportGenerator.setTestCaseDescription(self, "Verify Login for multiple data")
        WebCommonMethods.openUrl(self, WebLocatorLibrary.MY_LEARNING_URL)

        MyLearningLogin.login(self, excel_data.get("UserName"), excel_data.get("Password"))


