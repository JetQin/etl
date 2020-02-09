from pyspark.sql import SparkSession
from reader import JsonReader, MariadbReader, CassandraReader

if __name__ == '__main__':

    spark = SparkSession \
        .builder.master("local[*]")\
        .appName("Python Spark ETL") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    # jsonReader = JsonReader(spark)
    # data = jsonReader.readJson()
    # data.show()
    #
    # mariadbReader = MariadbReader(spark)
    # df = mariadbReader.readTable('ROLE')
    # df.select('ROLE_NAME').show()

    cassandraReader = CassandraReader(spark)
    cassandraDF = cassandraReader.readTable('stock_history', 'dev')
    total = cassandraDF.select("code").count()
    print(total)

    cassandraDF.groupBy("code").count().show(500, False)
    # peopleDF = spark.read.json("data/people.json")
    # # DataFrames can be saved as Parquet files, maintaining the schema information.
    # peopleDF.write.parquet("data/people.parquet")
    #
    # # Read in the Parquet file created above.
    # # Parquet files are self-describing so the schema is preserved.
    # # The result of loading a parquet file is also a DataFrame.
    # parquetFile = spark.read.parquet("data/people.parquet")
    #
    # # Parquet files can also be used to create a temporary view and then used in SQL statements.
    # parquetFile.createOrReplaceTempView("parquetFile")
    # teenagers = spark.sql("SELECT name FROM parquetFile WHERE age >= 13 AND age <= 19")
    # teenagers.show()

    spark.stop()


