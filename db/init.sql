CREATE DATABASE dc_heroes;
\c dc_heroes;
CREATE TABLE IF NOT EXISTS SUPER_HEROE(
    id SERIAL NOT NULL,
    name varchar(50),
    full_name varchar(200),
    alter_egos varchar(200),
    aliases varchar(200),
    place_of_birth varchar(200),
    first_appearance varchar(200),
    publisher varchar(200),
    alignment varchar(200),
    gender varchar(200),
    race varchar(200),
    height varchar(200),
    weight varchar(200),
    eye_color varchar(200),
    hair_color varchar(200),
    occupation varchar(500),
    base varchar(500),
    group_affiliation varchar(500),
    relatives varchar(500),
    image varchar(500),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS SUPERHEROES_STATS(
    id integer ,
    intelligence integer,
    strength integer,
    speed integer,
    durability integer,
    power integer,
    COMBAT integer,
    PRIMARY KEY (id)
);