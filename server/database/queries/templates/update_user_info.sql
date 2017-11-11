UPDATE users
SET display_name = :display_name, hashed_password = :hashed_password
RETURNING *
