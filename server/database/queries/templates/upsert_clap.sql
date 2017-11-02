WITH
old_clap AS (
    SELECT claps.amount
    FROM claps
    WHERE claps.user_id = :user_id AND claps.post_id = :post_id
),
new_clap AS (
    INSERT INTO claps (user_id, post_id, amount)
    VALUES (:user_id, :post_id, LEAST(:amount, 50))
    ON CONFLICT (user_id, post_id) DO
    UPDATE SET amount = LEAST(claps.amount + :amount, 50)
    WHERE claps.user_id = :user_id AND claps.post_id = :post_id
    RETURNING claps.amount
)
UPDATE posts
SET total_claps = total_claps + (SELECT SUM(amount) FROM new_clap) - COALESCE((SELECT SUM(amount) FROM old_clap), 0)
WHERE posts.id = :post_id
RETURNING *;
