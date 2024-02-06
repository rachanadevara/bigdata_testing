import datetime
import os
import socket
import json

import configparser
import pytest
from self import self

from driver.DriverManager import DriverManager
from reusables.Defect import Defect
from reusables.ReportGenerator import ReportGenerator



def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        if result.failed:
            defectSummary = result.head_line.split(".", 1)[0]
            defectDescription = "Error occurred at"+str(result.longrepr.reprcrash.message)

            config = configparser.RawConfigParser()
            config.read(DriverManager.framework_path + '/tests/resources/inputs/config.properties')
            ReportGenerator.testCaseStatus = "FAILED"
            ReportGenerator.testStepsStatus = "FAILED"

            if config.get('details', 'TestManagementTool').casefold() == "ALM".casefold():
                defectId = Defect.raiseDefectinALM(self, "Defect while executing : " + defectSummary,
                                                   str(defectDescription))
                DriverManager.defectId = defectId

        item.session.results[item] = result


def pytest_addoption(parser):
    parser.addoption("--browserArg", action="store", default="default", help="Browser value from HP ALM")


def pytest_html_report_title(report):
    report.title = "Torchbearer Test Automation Framework - Test Report"


def pytest_configure(config):
    config._metadata.pop("JAVA_HOME", "None")
    config._metadata.pop("Plugins")
    config._metadata.pop("Packages")
    config._metadata['User Name'] = os.environ['USERNAME']
    config._metadata['Host Name'] = socket.gethostname()
    current_time = datetime.datetime.now()
    config._metadata['Execution Start Time'] = current_time.strftime("%d-%m-%Y %H:%M:%S")
    os.environ['execution_start_time'] = current_time.strftime("%d_%m_%Y_%H_%M_%S")
    os.environ["BrowserValue"] = config.getoption('--browserArg')
    if not config.option.htmlpath:
        config.option.htmlpath = config.rootdir + "/Outputs/TestResult_" + os.environ[
            'execution_start_time'] + "/HtmlTestReport.html"


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Execution End Time"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    passed_count = sum(1 for result in session.results.values() if result.passed)
    failed_count = sum(1 for result in session.results.values() if result.failed)

    test_execution_summary = {'Total': (passed_count + failed_count), 'Passed': passed_count, 'Failed': failed_count,
                              'Start Time': session.config._metadata['Execution Start Time'],
                              'End Time': session.config._metadata["Execution End Time"]}

    with open(DriverManager.framework_path + "/Outputs/notification.json", 'w') as f:
        json.dump(test_execution_summary, f)
    f.close()
