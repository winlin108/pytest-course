

class Point():
    def __init__(self, name, latitude, longitude):
        if not type(name) == str:
            raise TypeError("Invalid name. Name must be string.")
        self._name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self._latitude = latitude
        self._longitude = longitude


    def get_name(self):
        return self._name


    def get_lat_long(self):
        return (self._latitude, self._longitude)


class Map():
    def __init__(self, name, points) -> None:
        if not type(name) == str:
            raise TypeError("Invalid name. Name must be string.")
        self._name = name

        # add point to list
        self._points = points
        

    def get_points(self) -> list:
        return self._points
    