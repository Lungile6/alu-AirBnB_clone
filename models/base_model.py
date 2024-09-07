#!/usr/bin/python3
"""
BaseModel module
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class for other models to inherit from.
    Provides unique id, creation and update timestamps, and serialization to dictionary.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        Generates a unique id and sets the creation and update timestamps.
        """
        self.id = str(uuid.uuid4())  # Generate a unique id for the instance
        self.created_at = datetime.utcnow()  # Set the creation timestamp
        self.updated_at = datetime.utcnow()  # Set the update timestamp

    def save(self):
        """
        Updates the update timestamp to the current time.
        """
        self.updated_at = datetime.utcnow()  # Update the timestamp

    def to_dict(self):
        """
        Converts the instance to a dictionary format.
        Includes the class name and timestamps in ISO format.
        """
        insta_dict = self.__dict__.copy()  # Copy the instance's dictionary
        insta_dict["__class__"] = self.__class__.__name__  # Add the class name
        insta_dict["created_at"] = self.created_at.isoformat()  # Convert creation timestamp to ISO format
        insta_dict["updated_at"] = self.updated_at.isoformat()  # Convert update timestamp to ISO format

        return insta_dict

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        class_name = self.__class__.__name__  # Get the class name
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)  # Format the string

if __name__ == "__main__":
    # Create an instance of BaseModel
    my_model = BaseModel()
    # Add custom attributes to the instance
    my_model.name = "My First Model"
    my_model.my_number = 89
    # Print the instance
    print(my_model)
    # Save the instance (update the timestamp)
    my_model.save()
    # Print the instance again to see the updated timestamp
    print(my_model)
    # Convert the instance to a dictionary
    my_model_json = my_model.to_dict()
    # Print the dictionary representation of the instance
    print(my_model_json)
    # Print each key-value pair in the dictionary
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
