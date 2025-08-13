CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

DROP TABLE IF EXISTS book_tracker;

CREATE TABLE book_tracker (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(50),
    assigned_date DATE NOT NULL,
    deadline DATE NOT NULL
);

#test
INSERT INTO book_tracker (book_title, author, genre, assigned_date, deadline)
VALUES ('Sample Book', 'Test Author', 'Comedy', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY));
