USE project;

SELECT * FROM students;
SELECT * FROM marks;

-- SELECT stu_id, AVG(marks) OVER() AS avg_mark FROM marks;
-- SELECT stu_id, sub_id, MAX(marks) OVER() FROM marks;
-- SELECT stu_id, sub_id, MIN(marks) OVER(ORDER BY marks ASC) FROM marks;
-- SELECT stu_id, sub_id, RANK() OVER(ORDER BY marks DESC) FROM marks;
-- SELECT stu_id, sub_id, DENSE_RANK() OVER(ORDER BY marks DESC) FROM marks;
-- SELECT stu_id, sub_id, RANK() OVER(PARTITION BY sub_id ORDER BY marks DESC) FROM marks;

SELECT st.stu_id, st.name, sb.sub_id, m.marks,
	RANK() OVER(PARTITION BY m.sub_id ORDER BY m.marks DESC) AS rank_assign,
	CASE 
		WHEN marks >= 80 THEN "A+"
        WHEN marks >= 60 THEN "A"
        WHEN marks >= 50 THEN "B"
        WHEN marks >= 35 THEN "C"
        ELSE "FAIL"
        END AS grade
        FROM marks m
        INNER JOIN students st ON st.stu_id = m.stu_id
        INNER JOIN subjects sb ON m.sub_id = sb.sub_id;
        
        