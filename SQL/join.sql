-- SHOW DATABASES;
-- USE project;
-- SHOW TABLES;
SELECT * FROM marks;
SELECT * FROM students;
SELECT * FROM subjects;

-- SELECT st.stu_id AS student_id, st.name AS student_name, sb.subject_name AS subject_name, m.marks
-- FROM students st
-- INNER JOIN marks m ON  m.stu_id = st.stu_id
-- INNER JOIN subjects sb ON m.sub_id = sb.sub_id;

-- SELECT st.stu_id AS student_ID, st.name AS student_Name, sb.subject_name AS subject_Name, m.marks
-- FROM students st
-- LEFT JOIN marks m ON m.stu_id = st.stu_id
-- LEFT JOIN subjects sb ON m.sub_id = sb.sub_id;

-- SELECT st.stu_id AS student_ID, st.name AS student_Name, sb.subject_name AS subject_Name, m.marks
-- FROM students st
-- RIGHT JOIN marks m ON m.stu_id = st.stu_id
-- RIGHT JOIN subjects sb ON m.sub_id = sb.sub_id;

SELECT st.stu_id AS student_ID, st.name AS student_Name, sb.subject_name AS subject_Name, m.marks
FROM students st
LEFT JOIN marks m ON m.stu_id = st.stu_id
LEFT JOIN subjects sb ON m.sub_id = sb.sub_id
UNION 
SELECT st.stu_id AS student_ID, st.name AS student_Name, sb.subject_name AS subject_Name, m.marks
FROM students st
RIGHT JOIN marks m ON m.stu_id = st.stu_id
RIGHT JOIN subjects sb ON m.sub_id = sb.sub_id;
