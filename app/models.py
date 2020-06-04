from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
db = PostgresqlExtDatabase(
    "dc_heroes",
    host = "dc_db",
    port = 5432,
    user = "postgres",
    password = "postgres", 
    )

class Super_heroe(Model):
    name = CharField()
    full_name = CharField()
    alter_egos = CharField()
    aliases = CharField()
    place_of_birth = CharField()
    first_appearance = CharField()
    publisher = CharField()
    alignment = CharField()
    gender = CharField()
    race = CharField()
    height = CharField()
    weight = CharField()
    eye_color = CharField()
    hair_color = CharField()
    occupation = CharField()
    base = CharField()
    group_affiliation = CharField()
    relatives = CharField()
    image = CharField ()

    class Meta:
        database = db
        db_table = 'SUPER_HEROE'