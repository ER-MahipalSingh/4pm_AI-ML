-- SHOW DATABASES;

-- CREATE DATABASE projet;
-- CREATE DATABASE project;
-- USE project;

-- CREATE TABLE students(
-- 	stu_id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(30) NOT NULL
-- );

-- CREATE TABLE subjects(
-- 	sub_id INT AUTO_INCREMENT PRIMARY KEY,
--     subject_name VARCHAR(30) NOT NULL
-- );

-- CREATE TABLE marks(
-- 	stu_id INT,
-- 	sub_id INT,
--     marks INT,
--     
--     PRIMARY KEY(stu_id, sub_id),
--     
--     FOREIGN KEY(stu_id) REFERENCES students(stu_id),
--     FOREIGN KEY(sub_id) REFERENCES subjects(sub_id)
-- );

-- INSERT INTO students(name)
-- VALUES
-- ("Ram"), ("Geeta"), ("Sita"), ("David"), ("Jhon");

-- INSERT INTO subjects(subject_name)
-- VALUES
-- ("Python"), ("Numpy"), ("Pandas"), ("JavaScript"), ("Nodejs");

-- INSERT INTO marks(stu_id, sub_id, marks)
-- VALUES
-- (1,2,85), (2,5,69),(1,3,78),(3,4,56),(4,2,78);

-- SELECT * FROM students;
-- SELECT * FROM subjects;
-- SELECT * FROM marks;
-- SHOW CREATE TABLE marks;

-- ALTER TABLE marks ADD CONSTRAINT fk_stu FOREIGN KEY(stu_id) REFERENCES students(stu_id) ON DELETE CASCADE;
-- ALTER TABLE marks ADD CONSTRAINT fk_sub FOREIGN KEY(sub_id) REFERENCES subjects(sub_id) ON DELETE CASCADE;