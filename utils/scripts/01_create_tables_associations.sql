DROP DATABASE IF EXISTS farmly;
CREATE DATABASE farmly;

\c farmly;


CREATE TABLE IF NOT EXISTS yard (
    yard_id INT GENERATED ALWAYS AS IDENTITY,
    yard_name VARCHAR(255),
    yard_location VARCHAR(255),
    PRIMARY KEY (yard_id)
);


CREATE TABLE IF NOT EXISTS bed (
    bed_id INT GENERATED ALWAYS AS IDENTITY,
    yard_id INT,
    PRIMARY KEY (bed_id),
    CONSTRAINT fk_bed_yard
      FOREIGN KEY (yard_id)
        REFERENCES yard(yard_id)
	  ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS plant (
    plant_id INT GENERATED ALWAYS AS IDENTITY,
    bed_id INT,
    PRIMARY KEY (plant_id),
    CONSTRAINT fk_plant_bed
      FOREIGN KEY (bed_id)
        REFERENCES bed(bed_id)
	  ON DELETE CASCADE
);


  GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO farmly_user;
