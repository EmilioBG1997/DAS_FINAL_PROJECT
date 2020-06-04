CREATE DATABASE dc_heroes;
\c dc_heroes;

CREATE TABLE SUPER_HEROE(
    id SERIAL NOT NULL,
    name VARCHAR(50),
    full_name VARCHAR(100),
    alter_egos VARCHAR(100),
    aliases VARCHAR(100),
    place_of_birth VARCHAR(100),
    first_appearance VARCHAR(100),
    publisher VARCHAR(100),
    alignment VARCHAR(100),
    gender VARCHAR(100),
    race VARCHAR(100),
    height VARCHAR(100),
    weight VARCHAR(100),
    eye_color VARCHAR(100),
    hair_color VARCHAR(100),
    occupation VARCHAR(500),
    base VARCHAR(500),
    group_affiliation VARCHAR(500),
    relatives TEXT,
    image VARCHAR(500),
    PRIMARY KEY(id)
);
CREATE TABLE SUPERHEROES_STATS(
    id integer ,
    intelligence integer,
    strength integer,
    speed integer,
    durability integer,
    power integer,
    COMBAT integer,
    PRIMARY KEY (id)
);