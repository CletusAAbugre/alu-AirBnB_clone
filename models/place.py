from models.base_model import BaseModel

class Place(BaseModel):
    city_id = ""  # References the city where the place is located
    user_id = ""  # References the user who created the place
    name = ""      # Name of the place
    description = ""  # Description of the place
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # List of Amenity IDs

