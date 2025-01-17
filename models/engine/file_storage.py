import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add new object to __objects."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                obj_class = globals()[class_name]
                self.__objects[key] = obj_class(**value)
        except FileNotFoundError:
            pass

