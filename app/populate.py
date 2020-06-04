from models import *
from api_request import DC_API

def main():
    api = DC_API()
    data = api.get_data()

    for i in data:
        Super_heroe.get_or_create(
            name = i.get("name"),
            full_name = i.get("full-name"),
            alter_egos = i.get("alter-egos"),
            aliases = i.get("aliases"),
            place_of_birth = i.get("place-of-birth"),
            first_appearance = i.get("first-appearance"),
            publisher = i.get("publisher"),
            alignment = i.get("alignment"),
            gender = i.get("gender"),
            race = i.get("race"),
            height = i.get("height"),
            weight = i.get("weight"),
            eye_color = i.get("eye-color"),
            hair_color = i.get("hair-color"),
            occupation = i.get("occupatin"),
            base = i.get("base"),
            group_affiliation = i.get("group-affiliation"),
            relatives = i.get("relatives"),
            image = i.get("image")
        )
if __name__ == "__main__":
    main()