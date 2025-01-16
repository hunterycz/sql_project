NUM_SUPPLIERS_BY_REGION = '''
SELECT Region, COUNT(*) AS num_of_suppliers
FROM Suppliers
GROUP BY Region
'''

NUM_SUPPLIERS_BY_COUNTRY = '''
SELECT Country, COUNT(*) AS num_of_suppliers
FROM Suppliers
GROUP BY Country
'''

NUM_OF_PRODUCTS_SUPPLIED = '''
SELECT s.CompanyName, COUNT(*) AS num_of_products_supplied
FROM Products p
LEFT JOIN Suppliers s
ON p.SupplierID = s.SupplierID
GROUP BY p.SupplierID
'''

TOP_5_COUNTRIES_ORDERS = '''
SELECT o.ShipCountry, COUNT(*) AS num_orders
FROM Orders o
GROUP BY o.ShipCountry
ORDER BY num_orders DESC
LIMIT 5;
'''

GERMANY_SHIPPING_POSTAL_CODES = '''
SELECT o.ShipPostalCode, COUNT(*) AS germany_shipping_postal_codes
FROM Orders o
WHERE o.ShipCountry IN ("Germany")
GROUP BY o.ShipPostalCode
'''

TOP_5_ORDERS_USA_CITIES = '''
SELECT o.ShipCity, COUNT(*) AS num_orders
FROM Orders o
WHERE o.ShipCountry IN ("USA")
GROUP BY o.ShipCity
LIMIT 5;
'''

TOP_5_ORDERS_COMPANIES_USA = '''
SELECT o.ShipName, COUNT(*) AS num_orders
FROM Orders o
WHERE o.ShipCountry IN  ("USA")
GROUP BY o.ShipName
LIMIT 5;
'''

ROUND_AVG_UNIT_PRICE_BY_SUPPLIER = '''
SELECT *, ROUND(AVG(UnitPrice), 2) AS avg_unit_price
FROM Products
GROUP BY SupplierID
'''

FLOOR_AVG_UNIT_PRICE_BY_SUPPLIER = '''
SELECT *, FLOOR(AVG(UnitPrice)) AS avg_num_price
FROM Products
GROUP BY SupplierID
'''

CIEL_AVG_UNIT_PRICE_BY_SUPPLIER = '''
SELECT *, CEIL(AVG(UnitPrice)) AS avg_num_price
FROM Products
GROUP BY SupplierID
'''

AVG_UNIT_PRICE_GREATER_THAN_20 = '''
SELECT *
FROM (
    SELECT *, ROUND(AVG(UnitPrice), 2) AS avg_unit_price
    FROM Products
    GROUP BY SupplierID
    )
WHERE avg_unit_price > 20
'''

AVG_UNIT_PRICE_CATEGORIES = '''
SELECT SupplierID,
       ROUND(AVG(UnitPrice), 2) AS avg_unit_price,
       CASE
           WHEN AVG(UnitPrice) > 20 THEN 'High'
           WHEN AVG(UnitPrice) > 10 THEN 'Mid'
           ELSE 'Low'
       END AS price_category
FROM Products
GROUP BY SupplierID;
'''

PRODUCT_SUPPLIERS_UNITPRICE = '''
SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM Products p
LEFT JOIN Suppliers s
ON p.SupplierID = s.SupplierID
'''

MAX_UNIT_PRICE = '''
SELECT p.ProductName, s.CompanyName, MAX(p.UnitPrice)
FROM Products p
LEFT JOIN Suppliers s
ON p.SupplierID = s.SupplierID
'''

MIN_UNIT_PRICE = '''
SELECT p.ProductName, s.CompanyName, MIN(p.UnitPrice)
FROM Products p
LEFT JOIN Suppliers s
ON p.SupplierID = s.SupplierID
'''

SELECT_ALL_PRODUCTS = '''
SELECT *
FROM Products
'''

SELECT_ALL_PRODUCTS_LIMIT_5 = '''
SELECT *
FROM Products
LIMIT 5;
'''
