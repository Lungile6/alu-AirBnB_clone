#!/usr/bin/python3
"""
FileStorage module for serializing and
deserializing instances to/from a JSON file.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage.
        Args:
            obj (BaseModel): The object to add.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)  # Fixed key format
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns all objects in storage.
        Returns:
             dict: A dictionary of all stored objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes objects to the JSON file
        """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for key, obj in all_objs.items():  # Fixed iteration over items
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to the objecrs, if the file exists.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)  # Properly instantiate using from_dict
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
