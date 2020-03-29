from pyspark.sql import SparkSession
from service.processor import CassandraReader

if __name__ == '__main__':

    spark = SparkSession \
        .builder.master("local[*]") \
        .appName("Python Spark ETL") \
        .getOrCreate()

    # jsonReader = JsonReader(spark)
    # model = jsonReader.readJson()
    # model.show()
    #
    # mariadbReader = MariadbReader(spark)
    # df = mariadbReader.readTable('ROLE')
    # df.select('ROLE_NAME').show()

    cassandraReader = CassandraReader(spark)
    cassandraDF = cassandraReader.readTable('stock_current', 'dev')
    total = cassandraDF.select("code").count()
    print(total)

    cassandraReader.writeTable(cassandraDF, 'stock_daily', 'dev')
    #
    # cassandraDF.groupBy("code").count().show(500, False)
    #

    spark.stop()


