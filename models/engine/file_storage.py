import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"  # File to store data
    __objects = {}  # Dictionary to store all objects
    
    def all(self, cls=None):
        """Returns all objects or objects of a specific class"""
        if cls:
            cls_name = cls.__name__
            return {key: value for key, value in self.__objects.items() if key.split('.')[0] == cls_name}
        return self.__objects
    
    def new(self, obj):
        """Adds a new object to the dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """Serializes objects to a JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)
    
    def reload(self):
        """Loads objects from the JSON file into the dictionary"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == "State":
                        self.new(State(**value))
                    elif class_name == "City":
                        self.new(City(**value))
                    elif class_name == "Amenity":
                        self.new(Amenity(**value))
                    elif class_name == "Place":
                        self.new(Place(**value))
                    elif class_name == "Review":
                        self.new(Review(**value))

# Create the global storage object
storage = FileStorage()
storage.reload()

