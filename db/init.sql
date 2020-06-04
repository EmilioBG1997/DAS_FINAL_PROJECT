CREATE SERVER DAS_SISTEMAS FOREIGN DATA WRAPPER "default";
CREATE DATABASE dc_heroes;
\c dc_heroes;
CREATE TABLE IF NOT EXISTS SUPER_HEROE(
    id SERIAL NOT NULL,
    name varchar(50),
    full_name varchar(100),
    alter_egos varchar(100),
    aliases varchar(100),
    place_of_birth varchar(100),
    first_appearance varchar(100),
    publisher varchar(100),
    alignment varchar(100),
    gender varchar(100),
    race varchar(100),
    height varchar(100),
    weight varchar(100),
    eye_color varchar(100),
    hair_color varchar(100),
    occupation varchar(200),
    base varchar(200),
    group_affiliation varchar(300),
    relatives varchar(300),
    image varchar(300),
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