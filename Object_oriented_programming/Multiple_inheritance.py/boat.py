from vehicle import Vehicle
class Boat(Vehicle):
    def __init__(self, boat_type="sail", distance_travelled=0, unit="miles"):
        super().__init__(distance_travelled, unit)
        self.boat_type = boat_type

    def voyage(self, distance):
        self.distance_travelled += distance

    def description(self):
        initial = super().description()
        return f"{initial} using a {self.boat_type}"

        