-- creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$ ;
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
        DECLARE project_id VARCHAR(255);
        SELECT id INTO project_id FROM projects WHERE project_name = name;
        IF project_id IS NULL THEN
                INSERT INTO projects (name) VALUES (project_name);
                SET project_id = LAST_INSERT_ID();
        END IF;
        INSERT INTO corrections VALUES (user_id, project_id, score);
END $$
DELIMITER ;
