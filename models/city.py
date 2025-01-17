from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""  # References the state to which the city belongs
    name = ""      # Name of the city


