import pytest

from driver.DriverManager import DriverManager
from reusables.DatabaseManager import DatabaseManager
from reusables.ReportGenerator import ReportGenerator

"""/************************************************************************************************************************
* Name of the Class   : TestTc06VerifyDatabaseConnection
* Description  : This class is used to validate the framework capability of executing database queries
*************************************************************************************************************************/"""

@pytest.mark.non_browser
class TestTc06VerifyDatabaseConnection(DriverManager, ReportGenerator):

    """/*****************************************************************************************************************
    * Name of the Function   : test_verify_database()
    * Description  : Test method to connect SQL database and execute a query
    ******************************************************************************************************************/"""

    def test_verify_database(self):
        ReportGenerator.setTestCaseDescription(self, "Verify the database connection")
        connection = DatabaseManager.create_jdbc_connection(self, "oracle")

        DatabaseManager.executequery_genaratecsv(self, connection,
                                     "SELECT TO_CHAR(SYSDATE, 'MM-DD-YYYY HH24:MI:SS') NOW from DUAL",
                                     "DatabaseResponse")



        connection.close()