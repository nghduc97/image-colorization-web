SELECT *
FROM posts
LEFT OUTER JOIN image_posts ON image_posts.post_id = posts.id
LEFT OUTER JOIN discuss_posts ON discuss_posts.post_id = posts.id
WHERE posts.hidden=false AND posts.type = :type
ORDER BY posts.total_claps DESC
OFFSET :offset
LIMIT :limit;
