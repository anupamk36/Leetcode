# Write your MySQL query statement below

with cte as (select customer_id, min(order_date) as first_order from Delivery group by customer_id)
select round(count(*)*100/(select count(distinct customer_id) from Delivery),2) as immediate_percentage
from Delivery d INNER JOIN
cte ON cte.customer_id = d.customer_id
where cte.first_order = d.customer_pref_delivery_date