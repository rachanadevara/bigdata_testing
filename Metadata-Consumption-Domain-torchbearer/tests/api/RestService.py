import json
import logging

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator


class RestService(DriverManager, ReportGenerator):

    def verifyResponse(self, response, expected_value):
        response_message = "-"

        try:
            json_object = json.loads(response.content)
            response_message = json_object["message"]
            assert response_message == expected_value
            ReportGenerator.captureTestEvidence(self, "Verify Email Service",
                                                "Email should be sent", response_message,
                                                "api")
        except AssertionError as ae:
            logging.info(f"AssertionError error: {ae}")
            ReportGenerator.testStepsStatus = "FAILED"
            ReportGenerator.testCaseStatus = "FAILED"
            ReportGenerator.captureTestEvidence(self, "Verify Email Service",
                                                "Email should be sent", response_message,
                                                "api")
            raise AssertionError
