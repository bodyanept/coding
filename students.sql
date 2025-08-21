
-- create
CREATE TABLE STUDENTS (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT (100) NOT NULL,
  age INT NOT NULL,
  group_id INT NOT NULL
);

CREATE TABLE `GROUPS` (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  group_name TEXT NOT NULL
);

CREATE TABLE COURSES (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  course_name TEXT NOT NULL,
  teacher_id INT NOT NULL
);

CREATE TABLE TEACHERS (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE ENROLLMENTS (
  student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  course_id INT NOT NULL,
  grade DECIMAL(3,2) NOT NULL,
  group_id INT NOT NULL
);

INSERT INTO STUDENTS (name, age, group_id) VALUES
('Иван Иванов', 22, 6),
('Анна Смирнова', 21, 5),
('Петр Кузнецов', 23, 1);


INSERT INTO `GROUPS` (group_name) VALUES
('ПСО'),
('УП'),
('СП');


INSERT INTO COURSES (course_name, teacher_id) VALUES
('папашлеп', 6),
('кутерьма', 5),
('да', 4);

INSERT INTO TEACHERS (name) VALUES
('Мария Ивановна'),
('Салават Сабирович'),
('Олег Монгол');

INSERT INTO ENROLLMENTS (course_id, grade, group_id) VALUES
(21, 5.0, 5),
(22, 4.6, 5),
(23, 3.3, 5);

SELECT * FROM STUDENTS;
SELECT * FROM `GROUPS`;
SELECT * FROM COURSES;
SELECT * FROM TEACHERS;
SELECT * FROM ENROLLMENTS;

SELECT s.name AS name, s.name, g.group_name
FROM STUDENTS s
JOIN `GROUPS` g ON s.name = g.group_name;
