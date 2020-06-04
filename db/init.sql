CREATE SERVER DAS_SISTEMAS FOREIGN DATA WRAPPER "default";
CREATE DATABASE dc_heroes;
CREATE TABLE IF NOT EXISTS SUPER_HEROE(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    full_name VARCHAR(100),
    ater_egos VARCHAR(100),
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
    occupation Varchar(200),
    base VARCHAR(200),
    group_affiliation VARCHAR(300),
    relatives VARCHAR(300),
    image varchar (300)
);

CREATE TABLE IF NOT EXISTS SUPERHEROES_STATS(
    id INTEGER PRIMARY KEY NOT NULL,
    intelligence Integer,
    strength INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    durability INTEGER NOT NULL,
    power INTEGER NOT NULL,
    COMBAT INTEGER NOT NULL
);