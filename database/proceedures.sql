DELIMITER $$
DROP PROCEDURE IF EXISTS `addTrains`$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE addTrains(
    IN Description VARCHAR(25)
)
BEGIN
    INSERT INTO trains
    (
        Description)
    VALUES
        (
        Description
        );

END$$
DELIMITER ;
