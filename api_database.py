from api_request import *
import sqlite3

db = sqlite3.connect("superheroes.db")
db_cursor = db.cursor()
api = DC_API()
data  = api.get_data()
def create_tables():
    query1 = '''
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
    '''
    query2 = '''
        CREATE TABLE IF NOT EXISTS SUPERHEROES_STATS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intelligence Integer,
            strength INTEGER NOT NULL,
            speed INTEGER NOT NULL,
            durability INTEGER NOT NULL,
            power INTEGER NOT NULL,
            COMBAT INTEGER NOT NULL
        );
    '''
    db_cursor.execute(query1)
    db_cursor.execute(query2)
    db.close()

def populate_tables():
    for i in data:
        ###TABLA_SUPERHEROES
        name = i['name']
        full_name = i['biography']['full-name']
        alter_egos = i['biography']['alter-egos']
        aliases = i['biography']['aliases']
        place_of_birth = i['biography']['place-of-birth']
        first_appearance = i['biography']['first-appearance']
        publisher = i['biography']['publisher']
        alignment = i['biography']['alignment']
        gender = i['appearance']['gender']
        race = i['appearance']['race']
        height = i['appearance']['height']
        weight = i['appearance']['weight']
        eye_color = i['appearance']['eye-color']
        hair_color = i['appearance']['hair_color']
        occupation =  i['work']['occupation']
        base = i['work']['base']
        group_affiliation = i['connections']['group-affiliation']
        relatives = i['connections']['relatives']
        image = i['image']['url']

        ##TALBA SUPERHEROES_STATS
        intelligence = i['powerstats']['intelligence']
        strenght = i['powerstats']['intelligence']
        speed = i['powerstats']['speed']
        durability = i['powerstats']['durability']
        power = i['powerstats']['power']
        combat = i['powerstats']['combat']

        query1 = f'''