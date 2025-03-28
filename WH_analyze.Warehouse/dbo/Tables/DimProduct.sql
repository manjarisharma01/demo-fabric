CREATE TABLE [dbo].[DimProduct] (

	[ProductKey] int NOT NULL, 
	[ProductAltKey] varchar(25) NULL, 
	[ProductName] varchar(50) NOT NULL, 
	[Category] varchar(50) NULL, 
	[ListPrice] decimal(18,0) NULL
);


GO
ALTER TABLE [dbo].[DimProduct] ADD CONSTRAINT UQ_efb14501_a2e6_4311_b77b_340776373932 unique NONCLUSTERED ([ProductKey]);