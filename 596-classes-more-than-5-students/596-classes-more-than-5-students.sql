# Write your MySQL query statement below

with cte as
(SELECT class, count(class)as numbers from Courses group by class) 
select class from cte where numbers >=5;