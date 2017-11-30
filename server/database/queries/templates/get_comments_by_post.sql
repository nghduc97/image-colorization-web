SELECT comments.*, users.display_name AS user_name
FROM comments
INNER JOIN users ON users.id = comments.user_id
WHERE comments.post_id = :post_id
ORDER BY comments.time;
