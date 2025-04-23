# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "warehouse": {
# META       "default_warehouse": "bbaea7a4-0d85-9fbd-4079-8e76906ac58b",
# META       "known_warehouses": [
# META         {
# META           "id": "bbaea7a4-0d85-9fbd-4079-8e76906ac58b",
# META           "type": "Datawarehouse"
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
# META   "language": "sql",
# META   "language_group": "sqldatawarehouse"
# META }

# CELL ********************

SELECT TOP (100) [CustomerKey],
			[CustomerAltKey],
			[Title],
			[FirstName],
			[LastName],
			[AddressLine1],
			[City],
			[StateProvince],
			[CountryRegion],
			[PostalCode]
FROM [AnalyzeData_WH].[dbo].[DimCustomer]

# METADATA ********************

# META {
# META   "language": "sql",
# META   "language_group": "sqldatawarehouse"
# META }
