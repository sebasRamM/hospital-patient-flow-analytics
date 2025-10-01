from pyspark.sql.functions import *


# Azure Event Hub Configuration
event_hub_namespace = <<Namespace_hostname>>
event_hub_name= <<Eventhub_name>>
event_hub_conn_str = <<Connect String>>


kafka_options = {
    'kafka.bootstrap.servers': f"{event_hub_namespace}:9093",
    'subscribe': event_hub_name,
    'kafka.security.protocol': 'SASL_SSL',
    'kafka.sasl.mechanism': 'PLAIN',
    'kafka.sasl.jaas.config': f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{event_hub_conn_str}";',
    'startingOffsets': 'latest',
    'failOnDataLoss': 'false'
}

# Read from eventhub
raw_df = (
    spark.readStream
    .format("kafka")
    .options(**kafka_options)
    .load()
)

# Cast data to JSON
json_df = raw_df.selectExpr("CAST(value AS STRING) as raw_json")

#ADLS configuration 
spark.conf.set(
  "fs.azure.account.key.<<Storage_Acount_Name>>.dfs.core.windows.net",
  <<Storage_Account_Access_Key>>
)

bronze_path = "abfss://<<container>>@<<Storage_Acount_Name>>.dfs.core.windows.net/patient_flow"

#Write stream to bronze
(
    json_df
    .writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "dbfs:/mnt/bronze/_checkpoints/patient_flow")
    .start(bronze_path)
)