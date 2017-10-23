INSERT INTO claps (user_id, post_id, amount)
VALUES (:user_id, :post_id, LEAST(:amount, 50))
ON CONFLICT (user_id, post_id) DO
UPDATE SET amount = LEAST(claps.amount + :amount, 50)
WHERE claps.user_id = :user_id AND claps.post_id = :post_id
RETURNING *;

-- TODO: update posts.total_claps
