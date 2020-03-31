from pyspark.sql import SparkSession
from service.processor import JsonReader


class ETLService:

    def __init__(self):
        self.session = SparkSession \
                .builder.master("local[*]") \
                .appName("Python Spark ETL") \
                .config("spark.some.config.option", "some-value") \
                .getOrCreate()
        self.reader = JsonReader()

    def execute(self):
        self.reader.readJson()
