# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "4e582aec-b368-4683-8df1-5e391e10a24f",
# META       "default_lakehouse_name": "LHwithSchema",
# META       "default_lakehouse_workspace_id": "2d4c04b6-12d4-42fe-9739-72511272f14a",
# META       "known_lakehouses": [
# META         {
# META           "id": "4e582aec-b368-4683-8df1-5e391e10a24f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT * FROM LHwithSchema.dbo.DimCustomer LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
