SELECT *
FROM discuss_posts
INNER JOIN posts ON hidden=false AND discuss_posts.post_id = posts.id
ORDER BY posts.total_claps DESC
OFFSET :offset
LIMIT :limit;
