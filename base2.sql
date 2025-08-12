
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50) NOT NULL
);



CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);


INSERT INTO groups (group_name) VALUES
('Художественная литература'),
('Научная фантастика'),
('Техническая литература');


INSERT INTO students (name, group_id) VALUES
('Иван Петров', 1),
('Мария Сидорова', 2),
('Алексей Иванов', 3),
('Елена Кузнецова', 1),
('Дмитрий Смирнов', 2);


SELECT 
    s.id AS student_id,
    s.name AS student_name,
    g.id AS group_id,
    g.group_name
FROM 
    students s
JOIN 
    groups g ON s.group_id = g.id;


SELECT 
    g.id AS group_id,
    g.group_name,
    COUNT(s.id) AS student_count
FROM 
    groups g
LEFT JOIN 
    students s ON g.id = s.group_id
GROUP BY 
    g.id, g.group_name
ORDER BY 
    g.id;


SELECT 
    g.id AS group_id,
    g.group_name,
    COUNT(s.id) AS student_count
FROM 
    groups g
JOIN 
    students s ON g.id = s.group_id
GROUP BY 
    g.id, g.group_name
HAVING 
    COUNT(s.id) > 2
ORDER BY 
    g.id;


ALTER TABLE students
ADD COLUMN enrollment_year INT NOT NULL DEFAULT 2023;
