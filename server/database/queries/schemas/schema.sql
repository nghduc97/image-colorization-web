DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    display_name VARCHAR(50),
    authority SMALLINT,
    username VARCHAR(32),
    hashed_password VARCHAR(150)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    hidden BOOLEAN,
    time TIMESTAMP,
    uploader_id INT REFERENCES users(id),
    title VARCHAR(100),
    type SMALLINT,
    total_claps INT
);

CREATE TABLE image_posts (
    post_id INT REFERENCES posts(id) PRIMARY KEY,
    status VARCHAR(20)
);

CREATE TABLE discuss_posts (
    post_id INT REFERENCES posts(id) PRIMARY KEY,
    content TEXT
);

CREATE TABLE comments (
    user_id INT REFERENCES users(id),
    post_id INT REFERENCES posts(id),
    time TIMESTAMP,
    content TEXT,
    PRIMARY KEY (user_id, post_id)
);

CREATE TABLE claps (
    user_id INT REFERENCES users(id),
    post_id INT REFERENCES posts(id),
    amount SMALLINT,
    PRIMARY KEY (user_id, post_id)
);

CREATE TABLE post_tag (
    post_id INT REFERENCES posts(id),
    tag VARCHAR(20),
    PRIMARY KEY (post_id, tag)
);
