from pathlib import Path

import pytest
import requests
import self as self

from driver.DriverManager import DriverManager
from reusables.ApiCommonMethods import ApiCommonMethods
from reusables.AuthenticationProvider import AuthenticationProvider
from reusables.ReportGenerator import ReportGenerator
from tests.api.ApiLibrary import ApiLibrary
from tests.api.RestService import RestService

"""/************************************************************************************************************************
* Name of the Class   : TestTc02VerifyRestServiceResponse
* Description  : This class is used to validate the framework capability of executing Test Email Service
*************************************************************************************************************************/"""

@pytest.mark.non_browser
class TestTc02VerifyRestServiceResponse(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_rest_api_2()
    * Description  : Test method for GSK Email service (REST)
    * @param requestBody : Request body retrieved from TestDataSheet
    ******************************************************************************************************************/"""

    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "frameworksanity", {"RequestBody"}))

    def test_rest_api(self, excel_data):
        ReportGenerator.setTestCaseDescription(self, "Test Email Service")
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


