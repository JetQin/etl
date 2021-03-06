from pyspark.sql.types import *


class CassandraReader:

    def __init__(self, spark=None):
        self.spark = spark

    def readTable(self, table, keyspace):

        return self.spark.read\
            .format("org.apache.spark.sql.cassandra")\
            .option("spark.cassandra.connection.host", "localhost")\
            .option("spark.cassandra.connection.port", "9042") \
            .option("spark.cassandra.auth.username", "cassandra") \
            .option("spark.cassandra.auth.password", "cassandra") \
            .option("keyspace", keyspace)\
            .option("table", table)\
            .load()

    def writeTable(self, data, table, keyspace):
        return data.write \
            .format("org.apache.spark.sql.cassandra") \
            .option("spark.cassandra.connection.host", "localhost") \
            .option("spark.cassandra.connection.port", "9042") \
            .option("spark.cassandra.auth.username", "cassandra") \
            .option("spark.cassandra.auth.password", "cassandra") \
            .option("keyspace", keyspace) \
            .option("table", table) \
            .save()
