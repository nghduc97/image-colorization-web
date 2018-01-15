WITH post AS (
    INSERT INTO posts (hidden, time, uploader_id, title, type, total_claps)
    VALUES (:hidden, :time, :uploader_id, :title, 2, :total_claps)
    RETURNING id
)
INSERT INTO discuss_posts (post_id, content)
VALUES ((SELECT id FROM post), :content)
RETURNING discuss_posts.post_id;
