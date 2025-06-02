-- Single-row
SELECT e.first_name, e.last_name, s.amount
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
WHERE s.amount > (
    SELECT MAX(s2.amount)
    FROM employees e2
    JOIN salaries s2 ON e2.employee_id = s2.employee_id
    WHERE e2.last_name = 'Wilson'
);

-- Multi-row
SELECT *
FROM employees
WHERE department_id <> 2
  AND role IN (
    SELECT DISTINCT role
    FROM employees
    WHERE department_id = 2
);


-- 
