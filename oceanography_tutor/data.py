"""
Oceanography Flashcard Tutor Data Models.

This module provides data models for tide, current, and salinity data,
as well as functions to access and manipulate this data.
"""

class Tide:
    """Represents a single tide reading."""
    def __init__(self, date, height):
        """
        Initializes a new tide reading.

        Args:
            date (str): Date of the tide reading in YYYY-MM-DD format.
            height (float): Height of the tide reading in meters.
        """
        self.date = date
        self.height = height

    def __repr__(self):
        return f"Tide(date='{self.date}', height={self.height})"


class Current:
    """Represents a single current reading."""
    def __init__(self, date, speed, direction):
        """
        Initializes a new current reading.

        Args:
            date (str): Date of the current reading in YYYY-MM-DD format.
            speed (float): Speed of the current reading in meters per second.
            direction (float): Direction of the current reading in degrees.
        """
        self.date = date
        self.speed = speed
        self.direction = direction

    def __repr__(self):
        return f"Current(date='{self.date}', speed={self.speed}, direction={self.direction})"


class Salinity:
    """Represents a single salinity reading."""
    def __init__(self, date, value):
        """
        Initializes a new salinity reading.

        Args:
            date (str): Date of the salinity reading in YYYY-MM-DD format.
            value (float): Value of the salinity reading in parts per thousand.
        """
        self.date = date
        self.value = value

    def __repr__(self):
        return f"Salinity(date='{self.date}', value={self.value})"


class DataStore:
    """Represents a store of tide, current, and salinity data."""
    def __init__(self):
        """
        Initializes an empty data store.
        """
        self.tides = []
        self.currents = []
        self.salinity = []

    def add_tide(self, tide):
        """
        Adds a new tide reading to the store.

        Args:
            tide (Tide): Tide reading to add.
        """
        self.tides.append(tide)

    def add_current(self, current):
        """
        Adds a new current reading to the store.

        Args:
            current (Current): Current reading to add.
        """
        self.currents.append(current)

    def add_salinity(self, salinity):
        """
        Adds a new salinity reading to the store.

        Args:
            salinity (Salinity): Salinity reading to add.
        """
        self.salinity.append(salinity)

    def get_tides(self):
        """Returns all tide readings in the store."""
        return self.tides

    def get_currents(self):
        """Returns all current readings in the store."""
        return self.currents

    def get_salinity(self):
        """Returns all salinity readings in the store."""
        return self.salinity
