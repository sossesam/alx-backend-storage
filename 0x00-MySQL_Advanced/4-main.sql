-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;
SELECT * FROM purchase;

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO purchase (item_name, number) VALUES ('pear', 6);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO purchase (item_name, number) VALUES ('apple', 7);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;
SELECT * FROM purchase;
