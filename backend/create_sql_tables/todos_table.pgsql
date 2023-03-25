CREATE TABLE IF NOT EXISTS todos (
    id BIGINT UNIQUE NOT NULL PRIMARY KEY, -- if you have PostgreSQL 7.3 or later, you can use the bigserial data type
    user_id INT, --later set not null
    is_complited BOOLEAN NOT NULL,
    todo_text TEXT NOT NULL
);

CREATE SEQUENCE todos_id_seq;

ALTER TABLE todos 
    ALTER COLUMN id 
        SET DEFAULT NEXTVAL('todos_id_seq');
