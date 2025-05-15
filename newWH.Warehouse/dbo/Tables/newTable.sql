CREATE TABLE [dbo].[newTable] (

	[SalesOrderKey] int NOT NULL, 
	[SalesOrderDateKey] int NOT NULL, 
	[ProductKey] int NOT NULL, 
	[CustomerKey] int NOT NULL, 
	[Quantity] int NULL, 
	[SalesTotal] decimal(18,0) NULL, 
	[ProductName] varchar(50) NULL, 
	[ListPrice] decimal(18,0) NULL
);