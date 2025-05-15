# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c366cdf2-c835-4520-898b-881796af5357",
# META       "default_lakehouse_name": "First_LH",
# META       "default_lakehouse_workspace_id": "8626a63c-37d4-429f-a5b6-a593a2d38dbb",
# META       "known_lakehouses": [
# META         {
# META           "id": "c366cdf2-c835-4520-898b-881796af5357"
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

df = spark.sql("SELECT * FROM First_LH.sales LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df2 = spark.read.format("csv").option("header","true").load("Files/data/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/data/sales.csv".
display(df2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
