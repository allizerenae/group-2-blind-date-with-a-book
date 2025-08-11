CREATE DATABASE IF NOT EXISTS LibraryDB;

USE LibraryDB;

CREATE TABLE book_tracker (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    Book_title VARCHAR(200) NOT NULL,
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Assigned_date DATE,
    Deadline DATE
);
