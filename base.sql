
-- create
CREATE TABLE authors (
  id INT NOT NULL AUTO_INCREMENT,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE publishers (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE books (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  author_id  INT,
  publisher_id  INT,
  year INT NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (author_id) REFERENCES authors(id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

-- insert
SELECT * FROM authors;
INSERT INTO authors (firstname,lastname) VALUES ('Clark', 'Sales');
INSERT INTO authors (firstname,lastname) VALUES ('Dave', 'Accounting');
INSERT INTO authors (firstname,lastname) VALUES ('Ava', 'Sales');

SELECT * FROM authors;

SELECT * FROM publishers;
INSERT INTO publishers (name) VALUES ('Эксмо');
INSERT INTO publishers (name) VALUES ('АCТ');
SELECT * FROM publishers;

SELECT * FROM books;
INSERT INTO books (title, author_id, publisher_id, year) 
VALUES ('SQL for Beginners', 1, 1, 2020);

INSERT INTO books (title, author_id, publisher_id, year) 
VALUES ('python', 2, 1, 2015);

INSERT INTO books (title, author_id, publisher_id, year) 
VALUES ('js for kids', 3, 2, 2011);

INSERT INTO books (title, author_id, publisher_id, year) 
VALUES ('base html', 1, 2, 2015);

SELECT * FROM books;
-- fetch 
SELECT title,year FROM books WHERE year = 2015;

UPDATE books SET year = 1998 WHERE id = 1;
SELECT * FROM books;

DELETE FROM books WHERE year < 2000;
SELECT * FROM books;


