CREATE DATABASE dc_heroes
CREATE TABLE IF NOT EXISTS SUPERHEROES(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    full-name VARCHAR(100),
    ater-egos VARCHAR(100),
    aliases VARCHAR(100),
    place_of_birth VARCHAR(100),
    first-appearance VARCHAR(100),
    publisher VARCHAR(100),
    alignment VARCHAR(100),
    gender VARCHAR(100),
    race VARCHAR(100),
    height VARCHAR(100),
    weight VARCHAR(100),
    eye-color VARCHAR(100),
    hair-color VARCHAR(100),
    occupation Varchar(200),
    base VARCHAR(200),
    group-affiliation VARCHAR(300),
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