import csv
import sys
import threading

from driver.DriverManager import DriverManager
from reusables.ReportGenerator import ReportGenerator


class DatabaseConnection(DriverManager):
    def executequery_genaratecsv(self, connection, query, databasename, filename=None):
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        framework_path = sys.path[0]
        if filename is not None:
            logs_file_path = framework_path + "/Outputs/TestResult_" + ReportGenerator.current_time + "/apilogs/" + str(
                threading.get_ident()) + "/" + filename + ".csv"
        else:
            logs_file_path = framework_path + "/Outputs/TestResult_" + ReportGenerator.current_time + "/apilogs/" + str(
                threading.get_ident()) + "/" + ReportGenerator.current_time + ".csv"
        file = open(logs_file_path, "w+", encoding="UTF-8", newline='')
        writer = csv.writer(file)
        writer.writerow(col[0] for col in cursor.description)
        for row in result:
            cleaned_row = [f'" {str(value)}"'.strip('"\'') for value in row]
            writer.writerow(cleaned_row)
        file.close()
        ReportGenerator.captureTestEvidence(self, "Verify if data is extracted from: " + str(databasename),
                                            str(databasename) + " Query should be executed successfully and data is extracted to csv file ",
                                            str(databasename) + " Query was executed successfully and data is extracted to csv file : " + str(
                                                filename) + ".csv",
                                            "")
        return logs_file_path
