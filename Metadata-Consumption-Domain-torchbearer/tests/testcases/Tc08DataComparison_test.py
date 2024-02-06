import pyodbc
import pytest
from _socket import gethostname
from assertpy import assert_that

from tests.Reusables.DatabaseConnections import DatabaseConnections
from reusables.DatabaseManager import DatabaseManager

from pathlib import Path
from self import self
from reusables.DataTesting import DataTesting
from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator

@pytest.mark.non_browser
class TestTc08DataComparison(DriverManager, ReportGenerator):
    @pytest.mark.parametrize("excel_data", DriverManager.dataProvider(self, Path(__file__).stem, "Sheet1", {"Denodo_Query", "Neo_Query","Nodes"}))
    def test_data_comparison_denodo_to_neo4j(self,excel_data):
        ReportGenerator.setTestCaseDescription(self, "CSV to CSV Comparison")
        neo4j_connection=DatabaseManager.create_neo4j_connection(self,"Neo4j")
        neo_df=DatabaseConnections.executequery_neo4j(self,neo4j_connection,excel_data.get("Neo_Query"),excel_data.get("Nodes"))
        neo_csv_file=DatabaseManager.generate_csv(self,neo_df,"Neo4j","Neodata")
        denodo_connection=DatabaseManager.create_denodo_connection(self,"Denodo")
        denodo_df=DatabaseManager.executequery_denodo(self,denodo_connection,excel_data.get("Denodo_Query"))
        denodo_csv_file=DatabaseManager.generate_csv(self,denodo_df,"Denodo","Denododata")
        status=DataTesting.csvcomparison(self,denodo_csv_file,neo_csv_file,[], "Neo4j","Denodo")
        assert_that(status).is_true()









