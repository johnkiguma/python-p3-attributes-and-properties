#!/usr/bin/env python3

#1.Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters. Your __init__ method should receive a default argument for name.
#If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."

#2.Define a breed property for your Dog class. Your __init__ method should receive a default argument for breed.
#If the breed is invalid, the setter method should print() "Breed must be in list of approved breeds." The breed must be in the following list of dog breeds:

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]


class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in approved_breeds:
            print("Breed must be in list of approved breeds.")
        self._breed = value.title()  # Convert breed to title case
