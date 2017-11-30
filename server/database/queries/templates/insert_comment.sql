WITH comment AS (
    INSERT INTO comments (user_id, post_id, time, content)
    VALUES (:user_id, :post_id, :time, :content)
    RETURNING *
)
SELECT comment.*, users.display_name AS user_name
FROM comment
INNER JOIN users ON users.id = comment.user_id;
