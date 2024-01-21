CREATE TABLE TASKS (
            id SERIAL PRIMARY KEY,
            title VARCHAR(20),
            description VARCHAR(100),
            created_at DATE,
            completed_at BOOLEAN DEFAULT FALSE,
            updated_at DATE DEFAULT NULL);

