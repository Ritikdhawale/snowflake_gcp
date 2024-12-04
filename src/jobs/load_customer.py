from src.utils.snowUtils import SnowFlakeConnector

account = "CYLVHGS-JO40980"
user = 'RITIKDHAWALE'
password = 'Ritik123'
warehouse = 'COMPUTE_WH'
database = 'test'
schema = 'sample'
role = 'SYSADMIN'

sf_connector = SnowFlakeConnector(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema,
    role=role
)

sf_connector.connect()

query = """
                select * from 
                SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER 
                LIMIT 10;
            """
result = sf_connector.execute_query(query=query)
print(result)
sf_connector.close_connection()
