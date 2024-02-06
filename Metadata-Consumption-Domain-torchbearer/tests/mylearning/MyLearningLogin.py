from time import sleep
import logging

from selenium.webdriver.common.by import By

from driver.DriverManager import DriverManager
from reusables.CommonUtilities import CommonUtilities
from reusables.ReportGenerator import ReportGenerator
from tests.mylearning.WebLocatorLibrary import WebLocatorLibrary


class MyLearningLogin(DriverManager):

    def login(self, user_name, password):
        try:

            if self.driver.title=="AccessGSK":

                self.driver.find_element(By.ID, WebLocatorLibrary.ID_USERNAME).send_keys(user_name)
                self.driver.find_element(By.ID, WebLocatorLibrary.ID_PASSWORD).send_keys(CommonUtilities.decrypt_Password(self,password))
                ReportGenerator.captureTestEvidence(self,
                                                    "mylearning  Login page",
                                                    "Username should be entered",
                                                    "Username was entered as " + user_name,
                                                    "web")
                self.driver.find_element(By.ID, WebLocatorLibrary.ID_SignIn).click()
                sleep(5)
                MyLearningLogin.myLearningHomePageValidation(self)

            elif self.driver.title.__contains__("Home"):
                MyLearningLogin.myLearningHomePageValidation(self)

            else:
                ReportGenerator.testStepsStatus = "FAILED"
                ReportGenerator.captureTestEvidence(self,
                                                    "MyLearning Home page",
                                                    "Verify web page title",
                                                    "Web page title was incorrect",
                                                    "web")

        except:
            ReportGenerator.captureErrorInfo(self, "web")


    def myLearningHomePageValidation(self):
        try:
            if self.driver.title.__contains__("Home"):
                ReportGenerator.captureTestEvidence(self,
                                                    "Mylearning Login page",
                                                    "User should login to mylearning application",
                                                    "User logged in successfully to mylearning application",
                                                    "web")
            else:
                ReportGenerator.testStepsStatus = "FAILED"
                ReportGenerator.captureTestEvidence(self,
                                                    "Mylearning Login page",
                                                    "User should login to mylearning application",
                                                    "User was not able to logged in to mylearning application",
                                                    "web")

        except Exception as ex:
            ReportGenerator.captureErrorInfo(self, "web")
            logging.error(f"Exception: {ex}")
