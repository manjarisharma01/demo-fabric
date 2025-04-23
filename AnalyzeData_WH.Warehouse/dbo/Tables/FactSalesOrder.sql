CREATE TABLE [dbo].[FactSalesOrder] (

	[SalesOrderKey] int NOT NULL, 
	[SalesOrderDateKey] int NOT NULL, 
	[ProductKey] int NOT NULL, 
	[CustomerKey] int NOT NULL, 
	[Quantity] int NULL, 
	[SalesTotal] decimal(18,0) NULL
);


GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_553fda76_0f13_4f19_b657_73715ee7b375 FOREIGN KEY ([ProductKey]) REFERENCES [dbo].[DimProduct]([ProductKey]);
GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_55fe1682_cccb_4503_8a93_f9b3923cb121 FOREIGN KEY ([SalesOrderDateKey]) REFERENCES [dbo].[DimDate]([DateKey]);
GO
ALTER TABLE [dbo].[FactSalesOrder] ADD CONSTRAINT FK_fbeb4768_07e8_4b01_acc3_0928bd1c6f04 FOREIGN KEY ([CustomerKey]) REFERENCES [dbo].[DimCustomer]([CustomerKey]);