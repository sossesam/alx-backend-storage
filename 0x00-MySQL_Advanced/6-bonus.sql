-- Check if the project exists
DELIMITER //

CREATE PROCEDURE AddBonus (
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score FLOAT
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    SELECT id INTO project_id 
    FROM projects 
    WHERE name = project_name LIMIT 1;

    -- If the project does not exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();  -- Get the ID of the newly created project
    END IF;

    -- Insert the correction for the user
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES (user_id, project_id, score);
END //

DELIMITER ;


