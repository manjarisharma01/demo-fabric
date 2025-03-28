-- Auto Generated (Do not modify) 6204512AC969558675CBDD79060FDCBDD4185A012A9EDD5201FAF7EE8DB580AD
CREATE VIEW [dbo].[vw_sample] AS (SELECT  d.[Year] AS CalendarYear,
         d.[Month] AS MonthOfYear,
         d.MonthName AS MonthName,
        SUM(so.SalesTotal) AS SalesRevenue
FROM FactSalesOrder AS so
JOIN DimDate AS d ON so.SalesOrderDateKey = d.DateKey
GROUP BY d.[Year], d.[Month], d.MonthName)