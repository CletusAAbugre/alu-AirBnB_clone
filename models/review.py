from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""  # References the place being reviewed
    user_id = ""   # References the user who wrote the review
    text = ""      # Text content of the review

