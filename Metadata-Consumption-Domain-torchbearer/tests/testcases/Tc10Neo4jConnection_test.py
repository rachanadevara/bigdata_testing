from neo4j import GraphDatabase

class Test_sample:

    def test_answer(self):

        neo4j_session = GraphDatabase.driver("neo4j+s://a47d1433.production-orch-0321.neo4j.io:7687", auth=("powerbi_read", "rdgreasungE1"))

        result = neo4j_session.session().run("MATCH (n:DataElement) where n.data_domain_instance_name=\"ddmp_dev\" AND n.dataset_name=\"dv_domain_details_extended_contract_partner\" RETURN n")

        for r in result:
            print(r.data())

        result = neo4j_session.session().run("CALL apoc.export.csv.query(\"MATCH (n:DataElement) " +
                                    "where n.dataset_name='bv_domain_tags' AND " +
                                    "n.data_domain_instance_name='ddmp_dev' " +
                                    "RETURN n.name\", \"result.csv\", {})")

        for r in result:
            print(r.data())



        neo4j_session.close()
