-- Creating a table to insert new imformation easier
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100), NOT NULL,
    major_subject VARCHAR(50), UNIQUE 
);

INSERT INTO Students (student_id, name, major_subject) VALUES
(1, 'John Smith', 'Computer Science'),
(2, 'Emily Johnson', 'Biology'),
(3, 'Michael Davis', 'Mathematics'),
(4, 'Jessica Brown', 'History'),
(5, 'Christopher Wilson', 'English'),
(6, 'Sarah Martinez', 'Psychology'),
(7, 'Daniel Thompson', 'Chemistry'),
(8, 'Amanda Garcia', 'Sociology'),
(9, 'James Hernandez', 'Political Science'),
(10, 'Olivia Lopez', 'Economics'),
(11, 'William Rodriguez', 'Physics'),
(12, 'Sophia Perez', 'Art History'),
(13, 'Benjamin Flores', 'Environmental Science'),
(14, 'Isabella Gonzalez', 'Communications'),
(15, 'Alexander Lewis', 'Anthropology'),
(16, 'Mia Lee', 'Foreign Languages'),
(17, 'Ethan Walker', 'Geology'),
(18, 'Charlotte Hall', 'Music'),
(19, 'Ryan Young', 'Engineering'),
(20, 'Madison Scott', 'Philosophy'),
(21, 'Jacob Green', 'Nursing'),
(22, 'Victoria King', 'Theater'),
(23, 'Matthew Turner', 'Business Administration'),
(24, 'Lily Hill', 'Marketing'),
(25, 'Andrew Cook', 'Astronomy');
