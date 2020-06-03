from models import *
from api_request import DC_API

def main():
    api = DC_API()
    data = api.get_data()

    for i in data:
        superheroe = SuperHeroe.get_or_create(
            name = i.get("name"),
            full_name = i.get("full-name"),
            alter_egos = i.get("alter-egos"),
            aliases = i.get("aliases"),
            place_of_birth = i.get("place-of-birth"),
            first_appearance = i.get("first-appearance"),
            publisher = i.get("publisher")
        )
if __name__ == "__main__":
    main()