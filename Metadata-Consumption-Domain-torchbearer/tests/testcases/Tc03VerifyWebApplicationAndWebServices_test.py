from pathlib import Path

import pytest
import requests
import self as self

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator
from reusables.WebCommonMethods import WebCommonMethods
from tests.mylearning.MyLearningLogin import MyLearningLogin
from tests.api.ApiLibrary import ApiLibrary
from reusables.AuthenticationProvider import AuthenticationProvider
from reusables.ApiCommonMethods import ApiCommonMethods
from tests.api.RestService import RestService
from tests.mylearning.WebLocatorLibrary import WebLocatorLibrary

"""/************************************************************************************************************************
* Name of the Class   : TestTc03VerifyWebApplicationAndWebServices
* Description  : This class is used to validate the integration framework capability for Web Application and Test Email Service
*************************************************************************************************************************/"""
@pytest.mark.frameworkSanity
class TestTc03VerifyWebApplicationAndWebServices(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_web_application_and_web_services()
    * Description  : Test method to verify Login for Web Application and Test Email Service
    * @param userName - Username retrieved from TestDataSheet
    * @param password - Password retrieved from TestDataSheet
    * @param requestBody - Request body retrieved from TestDataSheet
    ******************************************************************************************************************/"""


    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "frameworksanity",
                                                                      {"UserName", "Password", "RequestBody"}))
    def test_web_application_and_web_services(self, excel_data):
        ReportGenerator.setTestCaseDescription(self, "Verify Login for Web Application and Test Email Service")
        WebCommonMethods.openUrl(self, WebLocatorLibrary.MY_LEARNING_URL)
        MyLearningLogin.login(self, excel_data.get("UserName"), excel_data.get("Password"))
        request_headers = {'Content-Type': 'application/json'}
        request_params = {ApiLibrary.API_KEY: ApiLibrary.API_VALUE}
        filter_hooks = {"response": ReportGenerator.responseFilter}
        request_body = excel_data.get("RequestBody")
        ReportGenerator.api_name = "EmailAPI"
        response = requests.post(ApiLibrary.REST_URL,
                                 headers=request_headers,
                                 params=request_params,
                                 data=request_body,
                                 hooks=filter_hooks)
        is_valid_status = ApiCommonMethods.verifyStatusCode(self, response, "200", "Email Service API")
        if is_valid_status:
            RestService.verifyResponse(self, response, "Email sent successfully!")
