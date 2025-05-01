-- Всі продукти категорії 'Electronics’
SELECT product_id,product_name,category,price 
FROM products
WHERE category = 'Electronics';

-- Всі лієнти, email яких закінчується на 'example.com’
SELECT customer_id,first_name,last_name,email,phone,city,country
FROM customers
WHERE email LIKE '%@example.com';

-- Всі продукти, ціна яких між 50 і 150
SELECT product_id,product_name,category,price
FROM products
WHERE price BETWEEN 50 AND 150;

-- Всі товари, у яких назва починається на 'Product_1’
SELECT product_id,product_name,category,price
FROM products
WHERE product_name ILIKE '%Product_1%';

-- Всі працівників, у яких поле position заповнене (я назвав це поле role)
SELECT employee_id,first_name,last_name,role
FROM employees
WHERE role IS NOT NULL;

-- 2 додаткових запити з використанням предикатів
SELECT customer_id, first_name, last_name, country
FROM customers
WHERE country = 'Canada';

SELECT employee_id, first_name, last_name, hire_date
FROM employees
WHERE hire_date > '2025-01-01';

