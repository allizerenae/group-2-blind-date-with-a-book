
-- Create BookHistory table
CREATE TABLE BookHistory (
    Pk_history_id INT PRIMARY KEY AUTO_INCREMENT,
    Fk_member_id INT NOT NULL,
    Book_title VARCHAR(200) NOT NULL,
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Assigned_date DATE NOT NULL,
    Deadline DATE NOT NULL,
    FOREIGN KEY (Fk_member_id) REFERENCES Member(Pk_member_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);