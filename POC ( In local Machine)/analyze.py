from pyspark.sql import SparkSession
from pyspark.sql.functions import col,max,min,udf,to_timestamp,hour
from pyspark.sql.types import StringType
import pandas as pd

def Analyze_and_save():

    spark = SparkSession.builder \
        .appName("Analyze") \
        .getOrCreate()

    data = spark.read\
            .option("header",True)\
            .option("inferSchema",True)\
            .option("sep","\001")\
            .csv("/testingData/transformedData/")

    data = data.filter(data["number_of_shares"] != 'en')
    data = data.withColumn("time_stamp",to_timestamp("date_time","dd/MM/yyyy HH:mm"))
    data = data.withColumn("hour",hour("time_stamp"))

    # Insights to find out:
        # 1)authour and tweet with maximum likes
        # 2)count of positive tweets
        # 3)count of negative tweets
        # 4)Maximum tweets time

    # # 1)authour and tweet with maximum likes
    max_like = data.select(max(col("number_of_likes")))
    max_like = max_like.collect()
    max_liked = data.where(f"number_of_likes = {max_like[0][0]}")

    # 2)count of positive tweets
    grouped_df = data.groupBy("sentiment")
    postive_tweets = grouped_df.count().where("sentiment = 'Positive'")

    # 3)count of negative tweets
    negative_tweets = grouped_df.count().where("sentiment = 'Negative'")

    # 4)Maximum tweets time
    time_group = data.groupBy("hour").count()
    max_time_hit = time_group.select(max(col("count")))
    max_hit_hour = time_group.where(f"count = {max_time_hit.collect()[0][0]}")


    json_1 = max_liked.toJSON().collect()
    json_2 = postive_tweets.toJSON().collect()
    json_3 = negative_tweets.toJSON().collect()
    json_4 = max_hit_hour.toJSON().collect()

    Insights = {
        "max_liked" : json_1,
        "postive_tweets" : json_2,
        "negative_tweets" : json_3,
        "max_hit_hour" : json_4
    }


    df = pd.DataFrame(Insights)
    df.to_json("~/TestingDatas/output/insights.json")