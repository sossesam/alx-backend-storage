DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM scores
    WHERE user_id = user_id;

    -- Check if the user already has an average score recorded
    IF EXISTS (SELECT 1 FROM user_averages WHERE user_id = user_id) THEN
        -- Update the existing average score
        UPDATE user_averages 
        SET average_score = avg_score 
        WHERE user_id = user_id;
    ELSE
        -- Insert a new record for the user's average score
        INSERT INTO user_averages (user_id, average_score) 
        VALUES (user_id, avg_score);
    END IF;
END //

DELIMITER ;
