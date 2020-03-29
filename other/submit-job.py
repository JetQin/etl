
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder.master("local[*]") \
    .appName("Python Spark ETL") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read\
        .format("org.apache.spark.sql.cassandra")\
        .option("spark.cassandra.connection.host", "localhost")\
        .option("spark.cassandra.connection.port", "9042") \
        .option("spark.cassandra.auth.username", "cassandra") \
        .option("spark.cassandra.auth.password", "cassandra") \
        .option("keyspace", "dev")\
        .option("table", "stock_history")\
        .load()

# print total code
total_code = df.select("code").count()
print(total_code)

# list first 500 record
df.groupBy("code").count().show(500, False)
