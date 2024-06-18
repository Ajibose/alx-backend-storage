-- A script that creates a trigger that decreases the quantity in the items table
-- after adding a new order
CREATE TRIGGER decrease_quantity
AFTER INSERT
ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
