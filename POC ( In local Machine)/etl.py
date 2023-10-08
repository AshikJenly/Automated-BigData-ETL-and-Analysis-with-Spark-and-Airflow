from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
from textblob import TextBlob

def tranform_data():

    spark = SparkSession.builder \
        .appName("ETL") \
        .getOrCreate()

    data = spark.read\
            .option("header",True)\
            .option("inferSchema",True)\
            .csv("/testingData/tweets.csv")

    # Drop Null Values
    null_columns = ["country","language","latitude","longitude"]
    data = data.drop(*null_columns)
    data = data.na.drop()

    #returns sentiment of given text
    def getSentiment(text):
        analysis = TextBlob(text)
        return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    sentiment_udf = udf(getSentiment, StringType())

    data = data.withColumn("sentiment",sentiment_udf(data["content"]))


    data.write\
        .option("header",True)\
        .option("mode","overwrite")\
        .option("sep","\001")\
        .csv("/testingData/transformedData")
    data.show()