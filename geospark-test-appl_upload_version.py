import boto3
import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from geospark.register import GeoSparkRegistrator

if __name__ == "__main__":

    spark = SparkSession.builder.appName("GeoTestApp").getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')
    GeoSparkRegistrator.registerAll(spark)
    jdbc_url = 'jdbc:postgresql://XXXXXXXXXXX.us-west-2.rds.amazonaws.com/postgres?user=postgres&password=XXXXXXXXXXX'
    query = 'select name, ST_AsText(ST_Multi(wkb_geometry)) as wkb_geometry from public."us_states" where wkb_geometry is not null'
    state_df = spark.read.format("jdbc").option("url", jdbc_url).option("query", query).load()
    state_df.createOrReplaceTempView("state_table")
    state_geom = spark.sql("select name, ST_GeomFromText(wkb_geometry) as geom from state_table")
    state_geom.createOrReplaceTempView("state_geo_table")
    sample_df = spark.read.option("header", "true").option("inferSchema", value=True).csv("s3n://geospatial-source-bucket-nilabja/geo_samples.csv")
    sample_df.createOrReplaceTempView("sample_table")
    sample_geo_df = spark.sql("select id, lat, lon, rndm_measured_attr, ST_Point(CAST(lon as DECIMAL), CAST(lat as DECIMAL)) as geom from sample_table")
    sample_geo_df.createOrReplaceTempView("sample_geo_table")
    joined_df = spark.sql("select sample_geo_table.id, sample_geo_table.lat, sample_geo_table.lon, sample_geo_table.rndm_measured_attr, state_geo_table.name from sample_geo_table, state_geo_table where ST_Contains(state_geo_table.geom, sample_geo_table.geom)")
    folder_name = 'joined_state_classification_{}'.format(datetime.datetime.utcnow().strftime('%s'))
    joined_df.write.option("header","true").csv("s3a://geospatial-target-bucket-nilabja/{}".format(folder_name))
