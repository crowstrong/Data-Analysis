SELECT 
    s.name AS student_name,
    sv.title AS survey_title,
    sv.description AS reason,
    m.response_time
FROM meta_data m
JOIN students s ON m.student_id = s.id
JOIN surveys sv ON m.survey_id = sv.id;

SELECT 
    s.name,
    COUNT(m.survey_id) AS total_surveys
FROM meta_data m
JOIN students s ON m.student_id = s.id
GROUP BY s.name;

SELECT 
    s.name AS student_name,
    sk.name AS skill_name
FROM student_skills ss
JOIN students s ON s.id = ss.student_id
JOIN skills sk ON sk.id = ss.skill_id;

SELECT 
    st.name AS student_name,
    lg.name AS learning_goal
FROM learning_goals lg
LEFT JOIN student_learning_goals slg ON slg.goal_id = lg.id
LEFT JOIN students st ON st.id = slg.student_id
ORDER BY lg.name;