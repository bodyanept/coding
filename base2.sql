CREATE TABLE students  (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  group_id INT NOT NULL,
  PRIMARY KEY(id)
);


CREATE TABLE groups (
  id INT NOT NULL AUTO_INCREMENT,
  group_name VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);


ALTER TABLE students
ADD CONSTRAINT fk_students_groups
FOREIGN KEY (group_id) REFERENCES groups(id);

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
