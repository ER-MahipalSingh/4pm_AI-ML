USE project;

SELECT * FROM marks;
SELECT * FROM students;
SELECT * FROM subjects;

-- SELECT * FROM marks WHERE marks  > ( SELECT AVG(marks) FROM marks); 

-- SELECT name FROM students WHERE stu_id IN (SELECT stu_id from marks);

-- SELECT name FROM students WHERE stu_id IN (
-- 	SELECT stu_id FROM marks WHERE marks = (
-- 			SELECT MAX(marks) FROM marks
-- 		)
-- 	);

SELECT st.stu_id, st.name, (
	SELECT SUM(m.marks) FROM marks m 
		WHERE st.stu_id = m.stu_id
    ) AS total FROM students st;
    
    
    
	