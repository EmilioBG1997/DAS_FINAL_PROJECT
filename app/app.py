from flask import Flask, render_template
from models import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heroes")
def DcHeroes():
    dc = []
    for i in range(100):
        super_heroes = SUPER_HEROE.select().where(SUPER_HEROE.id == i)
        for hero in super_heroes:
            dc.append({
                "id":hero.id,
                "name":hero.name
                })
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
    