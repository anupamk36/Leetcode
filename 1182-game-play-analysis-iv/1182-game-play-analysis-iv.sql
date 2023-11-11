# Write your MySQL query statement below

SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM (
  SELECT player_id, event_date,
  MIN(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS firstlog
  FROM Activity
) AS a
WHERE DATEDIFF(a.event_date, a.firstlog) = 1;