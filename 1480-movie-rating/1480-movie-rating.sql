# Write your MySQL query statement below

with cte as(
select u.name, m.user_id, count(*) as 'total' from 
MovieRating m JOIN Users u
ON m.user_id = u.user_id  group by m.user_id
order by total desc, name limit 1),
# select name from cte;
cte2 as(
select m.title, mr.movie_id, avg(mr.rating) as 'average'
from MovieRating mr
JOIN Movies m ON
m.movie_id = mr.movie_id
WHERE mr.created_at like '2020-02-%'
GROUP BY m.movie_id
ORDER BY average DESC, m.title 
LIMIT 1
)

select name as results from cte 
UNION ALL 
SELECT title as results from cte2