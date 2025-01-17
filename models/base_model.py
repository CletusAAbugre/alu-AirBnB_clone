import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models"""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            # If we are given keyword arguments, initialize with those.
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Otherwise, assign default values.
            self.id = str(uuid.uuid4())  # Unique ID for each instance
            self.created_at = datetime.now()  # Timestamp for when the object is created
            self.updated_at = self.created_at  # Timestamp for the last time object was updated
    
    def save(self):
        """Updates the updated_at attribute and saves the object"""
        self.updated_at = datetime.now()
        storage.new(self)  # Save object to storage
        storage.save()     # Save to file
    
    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

