WITH post AS (
    INSERT INTO posts (hidden, time, uploader_id, title, type, total_claps)
    VALUES (:hidden, :time, :uploader_id, :title, 1, :total_claps)
    RETURNING id
)
INSERT INTO image_posts (post_id, status)
VALUES ((SELECT id FROM post), :status)
RETURNING image_posts.post_id;
