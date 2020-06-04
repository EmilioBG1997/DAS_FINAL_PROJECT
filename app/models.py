from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
db = PostgresqlExtDatabase(
    "dc_heroes",
    host = "dc_db",
    port = 5432,
    user = "postgres",
    password = "postgres", 
    )

class SUPER_HEROE(Model):
    name = TextField()
    full_name = TextField()
    alter_egos = TextField()
    aliases = TextField()
    place_of_birth = TextField()
    first_appearance = TextField()
    publisher = TextField()
    alignment = TextField()
    gender = TextField()
    race = TextField()
    height = TextField()
    weight = TextField()
    eye_color = TextField()
    hair_color = TextField()
    occupation = TextField()
    base = TextField()
    group_affiliation = TextField()
    relatives = TextField()
    image = TextField ()

    class Meta:
        database = db