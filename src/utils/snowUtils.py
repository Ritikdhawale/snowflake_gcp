import snowflake.connector


class SnowFlakeConnector:
    def __init__(self, account, user, password, warehouse, database, schema, role):
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.role = role

    def connect(self):
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema,
            role=self.role
        )
        self.cursor = self.connection.cursor()
        # self.cursor.execute(f"USE WAREHOUSE {self.warehouse}")


    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


# account = "CYLVHGS-JO40980"
# user = 'RITIKDHAWALE'
# password = 'Ritik123'
# warehouse = 'COMPUTE_WH'
# database = 'test'
# schema = 'sample'
# role = 'SYSADMIN'

# sf_connector = SnowFlakeConnector(
#     user=user,
#     password=password,
#     account=account,
#     warehouse=warehouse,
#     database=database,
#     schema=schema,
#     role=role
# )

# sf_connector.connect()

# query = """
#             select * from 
#             SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER 
#             LIMIT 10;
#         """
# result = sf_connector.execute_query(query=query)
# print(result)
# sf_connector.close_connection()
