from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, sum, window


# Initialize Spark Session
def main():
    spark = SparkSession.builder \
        .appName("REF_SMS Analysis") \
        .getOrCreate()

    # Load Data
    ref_data = spark.read.option("header", "true").csv("REF_CBS_SMS.csv")
    lookup_data = spark.read.option("header", "true").format("com.crealytics.spark.excel") \
        .option("inferSchema", "true").load("Ref.xlsx")

    # Convert Revenue to Tomans
    ref_data = ref_data.withColumn("REVENUE_TOMANS", col("DEBIT_AMOUNT_42") * 1000000)

    # Join with Lookup Table for Paytype
    lookup_data = lookup_data.withColumnRenamed("pay type", "PAYTYPE_515").withColumnRenamed("value", "PAYTYPE_VALUE")
    ref_data = ref_data.join(lookup_data, on="PAYTYPE_515", how="left")

    # Convert RECORD_DATE to Timestamp and extract day
    ref_data = ref_data.withColumn("RECORD_DATE", col("RECORD_DATE").cast("timestamp"))

    # 1. Daily Revenue Report
    daily_revenue = ref_data.groupBy(date_format("RECORD_DATE", "yyyy-MM-dd").alias("RECORD_DATE")) \
        .agg(sum("REVENUE_TOMANS").alias("DAILY_REVENUE"))

    # Save Daily Revenue Report to MinIO
    daily_revenue.write.csv("s3a://reports/daily_revenue.csv", header=True)

    # 2. Revenue by Paytype in 15-minute Intervals
    revenue_by_interval = ref_data.groupBy(
        window(col("RECORD_DATE"), "15 minutes"),
        col("PAYTYPE_VALUE")
    ).agg(sum("REVENUE_TOMANS").alias("REVENUE"))

    # Extract Start Time from Window
    revenue_by_interval = revenue_by_interval.withColumn("INTERVAL_START", col("window.start"))

    # Save Revenue by Interval Report to MinIO
    revenue_by_interval.select("INTERVAL_START", "PAYTYPE_VALUE", "REVENUE") \
        .write.csv("s3a://reports/revenue_by_interval.csv", header=True)
    spark.stop()


if __name__ == "__main__":
    main()
