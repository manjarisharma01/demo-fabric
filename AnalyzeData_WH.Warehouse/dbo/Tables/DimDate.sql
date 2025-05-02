CREATE TABLE [dbo].[DimDate] (

	[DateKey] int NOT NULL, 
	[DateAltKey] date NOT NULL, 
	[DayOfWeek] int NOT NULL, 
	[WeekDayName] varchar(10) NULL, 
	[DayOfMonth] int NOT NULL, 
	[Month] int NOT NULL, 
	[MonthName] varchar(12) NULL, 
	[Year] int NOT NULL
);


GO
ALTER TABLE [dbo].[DimDate] ADD CONSTRAINT UQ_1534d01e_e4fe_4225_8244_350f2a951cdb unique NONCLUSTERED ([DateKey]);