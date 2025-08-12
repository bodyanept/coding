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
