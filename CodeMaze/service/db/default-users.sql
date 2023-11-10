CREATE TABLE `codemaze`.`users` (`id` INT NOT NULL , `username` VARCHAR(255) NOT NULL , `pwd` VARCHAR(255) NOT NULL ) ENGINE = InnoDB;
CREATE TABLE `codemaze`.`flags` (`id` VARCHAR(255) NOT NULL , `vuln` VARCHAR(255) NOT NULL , `flag` VARCHAR(255) NOT NULL ) ENGINE = InnoDB;

INSERT INTO `users` (`id`, `username`, `pwd`) VALUES ('1', 'admin', 'CCIT{D3f4ult}');