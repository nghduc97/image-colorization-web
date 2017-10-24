INSERT INTO users (display_name, authority, username, hashed_password)
VALUES (:display_name, :authority, :username, :hashed_password)
RETURNING *;
