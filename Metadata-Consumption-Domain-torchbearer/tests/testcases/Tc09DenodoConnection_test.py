from fileinput import close
from pathlib import Path

from assertpy import assert_that
from reusables.DataTesting import DataTesting
from self import self

import pyodbc
import pytest
from _socket import gethostname
from driver.DriverManager import DriverManager
from reusables.DatabaseManager import DatabaseManager
from reusables.ReportGenerator import ReportGenerator
from tests.Reusables.DatabaseConnection import DatabaseConnection
from tests.Reusables.DatabaseManager import DatabaseManager
@pytest.mark.non_browser
class TestTc09TestDenodoConnection(DriverManager, ReportGenerator):

    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "Sheet_Denodo", {"Denodo_Query_1", "Denodo_Query_2"}))
    def test_data_comparison_from_denodo_to_denodo(self,excel_data):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")

        denodo_connection=DatabaseManager.create_denodo_connection(self,"Denodo")
        denodo_result=DatabaseManager.executequery_denodo(self,denodo_connection,excel_data.get("Denodo_Query_1"))
        denodofile_csv_query_expected=DatabaseManager.generate_csv(self,denodo_result,"Denodo","Denododata_01")
        denodo_result=DatabaseManager.executequery_denodo(self,denodo_connection,excel_data.get("Denodo_Query_2"))
        denodofile_csv_query_actual=DatabaseManager.generate_csv(self,denodo_result,"Denodo","Denododata_02")
        # denodofile_csv_query_expected = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"Select count(*) from denodometadata_dev.data_product","denodo","denodoexpectedfile")
        # denodofile_csv_query_actual = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"Select count(*) from denodometadata_dev.data_product","denodo","denodoactualfile")
        status=DataTesting.csvcomparison(self,denodofile_csv_query_expected, denodofile_csv_query_actual,[],"CSV","CSV")
        assert_that(status).is_true()

    def test_data_comparison_02(self):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")

        client_hostname = gethostname()
        useragent = "%s-%s" % (pyodbc.__name__, client_hostname)
        denodoserver_dsn ="DenodoODBC"
        denodo_connection = pyodbc.connect("DSN=%s;UserAgent=%s" % (denodoserver_dsn, useragent))
        denodofile_csv_query_expected= DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"SELECT COUNT(*) FROM GET_DATABASES()","denodo","denodoexpectedfile")
        denodofile_csv_query_actual = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"select count(*) from denodometadata_dev.data_domain_instance","denodo","denodoactualfile")
        status=DataTesting.csvcomparison(self,denodofile_csv_query_expected, denodofile_csv_query_actual,[],"CSV","CSV")
        assert_that(status).is_true()

    def test_data_comparison_03(self):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")

        client_hostname = gethostname()
        useragent = "%s-%s" % (pyodbc.__name__, client_hostname)
        denodoserver_dsn ="DenodoODBC"
        denodo_connection = pyodbc.connect("DSN=%s;UserAgent=%s" % (denodoserver_dsn, useragent))
        denodofile_csv_query_1 = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"SELECT db_name as name FROM GET_DATABASES() where db_name ='absorblms_dev'","denodo","denodofile1")
        denodofile_csv_query_2 = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"select name from denodometadata_dev.data_domain_instance WHERE name = 'absorblms_dev'","denodo","denodofile2")
        status=DataTesting.csvcomparison(self,denodofile_csv_query_1, denodofile_csv_query_2,[],"CSV","CSV")
        assert_that(status).is_true()

    def test_data_comparison_04(self):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")

        client_hostname = gethostname()
        useragent = "%s-%s" % (pyodbc.__name__, client_hostname)
        denodoserver_dsn ="DenodoODBC"
        denodo_connection = pyodbc.connect("DSN=%s;UserAgent=%s" % (denodoserver_dsn, useragent))
        denodofile_csv_query_1 = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"SELECT db_name as name FROM GET_DATABASES() where db_name ='absorblms_dev'","denodo","denodofile1")
        denodofile_csv_query_2 = DatabaseConnection.executequery_genaratecsv(self,denodo_connection,"select name from denodometadata_dev.data_domain_instance WHERE name = 'absorblms_dev'","denodo","denodofile2")
        status=DataTesting.csvcomparison(self,denodofile_csv_query_1, denodofile_csv_query_2,[],"CSV","CSV")
        assert_that(status).is_true()



