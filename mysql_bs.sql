CREATE TABLE movies IF NOT EXISTS (
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(50) NOT NULL,
	director VARCHAR(50),
	genres VARCHAR(50),
	year YEAR,
	description TEXT,
	imdb_id VARCHAR(11),
	imdb_score FLOAT(3),
	rotten_tomatoes_score INT(3),
    watch_status TINYINT(1),
	PRIMARY KEY(id)
);

CREATE TABLE watch_status IF NOT EXISTS (
	id INT NOT NULL AUTO_INCREMENT,
	movie_id INT NOT NULL,
    watch_status TINYINT(1),
	PRIMARY KEY(id)
);