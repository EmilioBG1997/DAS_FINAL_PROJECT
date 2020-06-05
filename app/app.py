from flask import Flask, render_template
from models import *
import redis
import json

client = redis.Redis(host='dc_redis', port=6379)
app = Flask(__name__)
cache_heroes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heroes")
def DcHeroes():
    dc = []
    
    if(not cache_heroes):
        for i in range(int(SUPER_HEROE.select().count())):
            print(f'vuelta {i}')
            data = SUPER_HEROE.get(SUPER_HEROE.id == i)
            data2 = SUPERHEROES_STATS.get(SUPERHEROES_STATS.id == i)
            dictionary = {
                "id": data.id,
                "name": data.name,
                "full_name": data.full_name,
                "alter_egos": data.alter_egos,
                "aliases": data.aliases,
                "place_of_birth": data.place_of_birth,
                "first_appearance": data.first_appearance,
                "publisher":data.publisher,
                "alignment": data.alignment,
                "gender": data.gender,
                "race": data.race,
                "height": data.height,
                "weigth": data.weight,
                "eye_color" : data.eye_color,
                "hair_color": data.hair_color,
                "occupation": data.occupation,
                "base": data.base,
                "group_affiliation":data.group_affiliation,
                "relatives": data.relatives,
                "image": data.image,
                "intelligence": data2.intelligence,
                "strength": data2.strength,
                "speed": data2.speed,
                "durability": data2.durability,
                "power": data2.power,
                "combat": data2.combat
            }
            valor = json.dumps(dictionary)
            llave = str(i)
            client.set(llave,valor)
            dc.append(dictionary)
            cache_heroes.append(llave)
    else:
        for i in cache_heroes:
            print(f"vuelta {i}")
            dc.append(json.loads(client.get(str(i))))

    return render_template("heroes.html" , dc=dc)

@app.route("/heroes/<hero>")
def Hero(hero):
    super_heroes = SUPER_HEROE.select().where(SUPER_HEROE.id == hero)
    super_stats = SUPERHEROES_STATS.select().where(SUPERHEROES_STATS.id == hero)
    for hero in super_heroes:    
        dc= {
                "id":hero.id,
                "name": hero.name,
                "full_name": hero.full_name,
                "alter_egos": hero.alter_egos,
                "aliases": hero.aliases,
                "place_of_birth": hero.place_of_birth,
                "first_appearance": hero.first_appearance,
                "publisher":hero.publisher,
                "alignment": hero.alignment,
                "gender": hero.gender,
                "race": hero.race,
                "height": hero.height,
                "weigth": hero.weight,
                "eye_color" : hero.eye_color,
                "hair_color": hero.hair_color,
                "occupation": hero.occupation,
                "base": hero.base,
                "group_affiliation":hero.group_affiliation,
                "relatives": hero.relatives,
                "image": hero.image
            }
    for stat in super_stats:
        dc_stats = {
            "intelligence": stat.intelligence,
            "strength": stat.strength,
            "speed": stat.speed,
            "durability": stat.durability,
            "power": stat.power,
            "combat": stat.combat
        }
    return render_template("hero.html", dc = dc, dc_stats=dc_stats)

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000)
    