import json
from models.base_model import BaseModel
import models  # Ensure models has a `classes` dictionary with all class mappings


class FileStorage:
    """Handles storage and retrieval of objects via JSON serialization."""
    
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Return the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """
        Add a new object to __objects.

        Args:
            obj (BaseModel): The object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.

        If the file does not exist or is empty, no action is taken.
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                obj_class = models.classes.get(class_name)
                if obj_class:  # Ensure the class exists in models.classes
                    self.__objects[key] = obj_class(**value)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

