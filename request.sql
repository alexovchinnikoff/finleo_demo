SELECT u.name AS user_name,
       COUNT(o.id) AS total_orders
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
GROUP BY u.id, u.name; 