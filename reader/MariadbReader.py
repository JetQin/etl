from pyspark.sql.types import *


class MariadbReader:

    def __init__(self, spark=None):
        self.spark = spark
        # self.schema = StructType([
        #     StructField("name", StringType()),
        #     StructField("age", IntegerType())
        # ])

    def readTable(self, table):

        return self.spark.read.format('jdbc').options(
            url="jdbc:mysql://localhost:3306/AUTH_SERVICE",
            driver="com.mysql.jdbc.Driver",
            dbtable=table,
            user="dbuser",
            password="dbuser"
        ).load()
