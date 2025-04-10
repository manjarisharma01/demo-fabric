# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "5b49bc85-1033-493a-ba93-73f49da6b8cb",
# META       "default_lakehouse_name": "lk_cicd",
# META       "default_lakehouse_workspace_id": "12d0fe46-a68c-47eb-88b9-50d05152e999",
# META       "known_lakehouses": [
# META         {
# META           "id": "5b49bc85-1033-493a-ba93-73f49da6b8cb"
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

df = spark.sql("SELECT * FROM lk_cicd.publicholidays LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
