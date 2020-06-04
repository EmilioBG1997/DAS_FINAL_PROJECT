from models import *
from api_request import DC_API


def main():
    api = DC_API()
    data = api.get_data()

    for i in data:
        Super_heroe.get_or_create(
            name = i.get("name"),
            full_name = i.get("biography",{}).get("full-name"),
            alter_egos = i.get("biography",{}).get("alter-egos")[0],
            aliases = i.get("biography",{}).get("aliases")[0],
            place_of_birth = i.get("biography",{}).get("place-of-birth"),
            first_appearance = i.get("biography",{}).get("first-appearance"),
            publisher = i.get("biography",{}).get("publisher"),
            alignment = i.get("biography",{}).get("alignment"),
            gender = i.get("appearance",{}).get("gender"),
            race = i.get("appearance",{}).get("race"),
            height = i.get("appearance",{}).get("height")[1],
            weight = i.get("appearance",{}).get("weight")[1],
            eye_color = i.get("appearance",{}).get("eye-color"),
            hair_color = i.get("appearance",{}).get("hair-color"),
            occupation = i.get("work",{}).get("occupatin"),
            base = i.get("work",{}).get("base"),
            group_affiliation = i.get("connections",{}).get("group-affiliation"),
            relatives = i.get("connections",{}).get("relatives"),
            image = i.get("image",{}).get("url")
        )
if __name__ == "__main__":
    main()