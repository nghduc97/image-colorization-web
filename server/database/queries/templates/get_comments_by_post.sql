SELECT *
FROM comments
WHERE comments.post_id = :post_id
ORDER BY comments.time;
