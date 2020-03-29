from pyspark.sql.types import *


class JsonReader:

    def __init__(self, spark=None):
        self.spark = spark
        self.schema = StructType([
            StructField("name", StringType()),
            StructField("age", IntegerType())
        ])

    def readJson(self):

        return self.spark.read.schema(self.schema)\
            .json("./model/test.json")