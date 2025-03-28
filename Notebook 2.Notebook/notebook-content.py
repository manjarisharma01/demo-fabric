# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b8a34596-e206-48d3-a062-6a22abb3ec43",
# META       "default_lakehouse_name": "demoCICDLH",
# META       "default_lakehouse_workspace_id": "38e521aa-f917-463b-a641-e8e24be1e8d5",
# META       "known_lakehouses": [
# META         {
# META           "id": "b8a34596-e206-48d3-a062-6a22abb3ec43"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM demoCICDLH.green_tripdata_2017 LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
