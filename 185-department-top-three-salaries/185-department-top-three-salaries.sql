# Write your MySQL query statement below
SELECT Department.Name AS "Department", e.Name as "Employee", e.Salary as "Salary" FROM
(SELECT departmentId, Name, Salary, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY Salary DESC) AS r
FROM Employee) e
JOIN Department ON e.departmentId = Department.id
WHERE r <= 3;