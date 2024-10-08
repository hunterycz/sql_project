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
