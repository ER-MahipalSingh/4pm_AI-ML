-- SHOW DATABASES;

-- CREATE DATABASE students_project;

-- SHOW DATABASES;

-- USE students_project;

-- CREATE TABLE students(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(30) NOT NULL,
--     subject VARCHAR(30) NOT NULL,
--     marks INT NOT NULL
-- );

-- INSERT INTO students(name, subject, marks)
-- VALUES
-- ("David", "Python", 85),
-- ("Jhon", "JavaScript", 92),
-- ("Alisa", "JavaScript", 66),
-- ("Ramesh", "Python", 45),
-- ("Radha", "Numpy", 55),
-- ("Sita", "Pandas", 69);

-- SELECT * FROM students;


-- SELECT * FROM students WHERE id = 5;
-- SELECT * FROM students WHERE marks >= 80;

-- SELECT subject, AVG(marks) as Average FROM students GROUP BY subject HAVING AVG(marks) >= 70;
-- SELECT subject, SUM(marks) as Sum FROM students GROUP BY subject;
-- SELECT subject, MIN(marks) FROM students GROUP BY subject;

-- SELECT * FROM students ORDER BY marks DESC;
-- SELECT * FROM students ORDER BY marks DESC LIMIT 3;
-- SELECT * FROM students ORDER BY marks ASC LIMIT 3;

-- SELECT * FROM students WHERE marks >= 30 AND marks <= 70;
-- SELECT * FROM students WHERE marks >= 300 OR marks <= 70;
SELECT * FROM students WHERE NOT marks >= 70;
