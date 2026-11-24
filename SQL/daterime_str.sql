-- USE project;

SELECT * FROM students;
SELECT * FROM marks;



-- ALTER TABLE marks ADD COLUMN exam_date DATE;
-- ALTER TABLE marks ADD COLUMN exam_time TIME;
-- ALTER TABLE marks ADD COLUMN created_at DATETIME;
-- DESC marks;

-- UPDATE marks SET exam_date = '2026-11-20' WHERE stu_id = 1;
-- UPDATE marks SET exam_time = NOW() WHERE stu_id = 1;
-- UPDATE marks SET created_at = NOW() WHERE stu_id = 1;
-- UPDATE marks SET exam_date = '2026-11-20' WHERE stu_id = 2;
-- UPDATE marks SET exam_date = '2025-11-20' WHERE stu_id = 3;
-- UPDATE marks SET exam_date = '2024-11-20' WHERE stu_id = 4;

-- SELECT * FROM marks WHERE YEAR(exam_date) = 2025;
-- SELECT * FROM marks WHERE exam_date >= DATE_SUB(CURDATE(), INTERVAL  2 YEAR) AND exam_date <= CURDATE();

-- SELECT * FROM marks;


-- SELECT UPPER(name) FROM students;
-- SELECT LOWER(name) FROM students;
-- SELECT LENGTH(name) FROM students;
-- SELECT CONCAT(stu_id, " - ", name) AS new_name FROM students;
-- SELECT SUBSTRING(name, 2,4) FROM students;


SELECT UPPER(st.name), m.marks,
	DATE_FORMAT(m.exam_date, "%d-%m-%Y") 
    FROM students st
	INNER JOIN marks m ON st.stu_id = m.stu_id;
