-- Создание таблицы customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) DEFAULT 'ВАНЬКА',
    phone VARCHAR(15) DEFAULT '8888888888'
);

-- Просмотр структуры таблицы customers
DESCRIBE customers;

-- Создание таблицы pizzas
CREATE TABLE pizzas (
    pizza_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    price DECIMAL(5,2) CHECK (price >= 0)
);

-- Создание таблицы employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    role VARCHAR(30),
    salary DECIMAL(8,2) CHECK (salary > 0)
);

-- Создание таблицы orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    employee_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Создание таблицы order_items
CREATE TABLE order_items (
    order_id INT,
    pizza_id INT,
    quantity INT CHECK (quantity > 0),
    PRIMARY KEY (order_id, pizza_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id)
);

-- Вставка данных в customers
INSERT INTO customers (name, phone)
VALUES 
('Анна Иванова', '89990001122'),
('Петр Смирнов', '89990003344'),
('Сергей Кузнецов', '89990005566');

-- Просмотр данных из customers
SELECT * FROM customers;

-- Вставка данных в employees
INSERT INTO employees (name, role, salary)
VALUES
('Мария Петрова', 'Повар', 45000.00),
('Игорь Соколов', 'Курьер', 40000.00);

-- Вставка данных в pizzas
INSERT INTO pizzas (title, price)
VALUES
('Маргарита', 400.00),
('Пепперони', 500.00),
('С ветчиной и сыром', 650.00);



INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (1, CURDATE(), 2);


INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(LAST_INSERT_ID(), 1, 1),
(LAST_INSERT_ID(), 2, 1);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (2, CURDATE(), 1);


INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(LAST_INSERT_ID(), 3, 2);

UPDATE pizzas
SET price = price * 1.15;

SELECT * FROM pizzas;

-- -- Изменение телефона читателя
UPDATE customers
SET phone = '89998887766'
WHERE customer_id = 3;

-- -- Добавление нового столбца
ALTER TABLE pizzas
ADD category VARCHAR(30);

UPDATE pizzas
SET category = CASE 
    WHEN title = 'Пепперони' THEN 'Острая'
    WHEN title = 'Маргарита' THEN 'Классическая'
    WHEN title = 'С ветчиной и сыром' THEN 'Сочная'
END;

CREATE TABLE suppliers (
    supplier_id  INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(20)
);

INSERT INTO suppliers (name, phone)
VALUES
('Zotman"', '89997778899'),
('Пиццман и Калачев', '89996665544');

ALTER TABLE pizzas
ADD supplier_id INT;

ALTER TABLE pizzas
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (1, 2);
UPDATE pizzas SET supplier_id = 2 WHERE pizza_id = 3;

SELECT * FROM pizzas;

SELECT o.order_id, c.name AS reader_name, e.name AS employees_name, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN employees e ON o.employee_id = e.employee_id;

DELETE FROM orders
WHERE order_date < CURDATE();

DELETE FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);

TRUNCATE TABLE suppliers;
DROP TABLE suppliers;
