# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "64904969-2dfa-46c1-aca8-e355bd06bf44",
# META       "default_lakehouse_name": "stagingLH",
# META       "default_lakehouse_workspace_id": "2d4c04b6-12d4-42fe-9739-72511272f14a",
# META       "known_lakehouses": [
# META         {
# META           "id": "64904969-2dfa-46c1-aca8-e355bd06bf44"
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

df = spark.sql("SELECT * FROM stagingLH.staging_sales LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
