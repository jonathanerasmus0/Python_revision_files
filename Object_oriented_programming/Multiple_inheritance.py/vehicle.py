class Vehicle:
    def __init__(self, distance_travelled=0, unit="miles"):
        self.distance_travelled = distance_travelled
        self.unit = unit
    
    def description(self):
        return f"A {self.__class__.__name__} that has travelled {self.distance_travelled} {self.unit}"
    
    