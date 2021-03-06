DELIMITER //
CREATE PROCEDURE EPOC_INSERT_VAL (IN IN_DATE date)
BEGIN
    DECLARE start_index INT DEFAULT 0;
	DELETE FROM EPOC_INSERT WHERE CDATE=IN_DATE;
    WHILE start_index < 86400 DO
	INSERT INTO EPOC_INSERT(CDATE,CSEC) VALUES (IN_DATE,UNIX_TIMESTAMP(IN_DATE)+start_index);
	set start_index = start_index+60;
    END WHILE;
END  //

;
