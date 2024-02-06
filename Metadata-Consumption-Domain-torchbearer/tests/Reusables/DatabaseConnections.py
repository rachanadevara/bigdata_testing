from driver.DriverManager import DriverManager
import pandas as pd

class DatabaseConnections(DriverManager):
   def executequery_neo4j(self, connection, query, nodes=None):
        result = connection.session().run(query)
        keys = result.keys()
        if all(key in keys for key in ['n', f'n.{keys[0]}']):
            result_list = [dict(record['n'], **{keys[0]: record[f'n.{keys[0]}']}) for record in result]
        elif 'n' in keys:
            result_list = [dict(record['n']) for record in result]
        else :
            nodes=[]
            if nodes is not None and len(nodes)>0 :
                result_list = []
                for record in result:
                    result_dict = {}
                    for node_type in nodes:
                            node_props = record[node_type].items()
                            for key, value in node_props:
                                result_dict[f"{node_type}.{key}"] = value
                    result_list.append(result_dict)
            else:
                result_list=[]
                for r in result:
                    result_dict = {}
                    for key, value in r.items():
                        result_dict[key.replace('n.','')] = value
                    result_list.append(result_dict)
        dataframe = pd.DataFrame(result_list)
        return dataframe
