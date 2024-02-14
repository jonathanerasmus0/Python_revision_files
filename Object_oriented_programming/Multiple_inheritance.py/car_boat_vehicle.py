from boat import Boat
from car import Car

class Carboatvehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_travelled=0, unit="miles"):
        super().__init__(engine, tires, distance_travelled, unit)
        self.boat_type = "motor"
    
    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)
    
    def __str__(self):
        return f"Carboatvehicle with engine: {self.engine}, tires: {self.tires}, distance travelled: {self.distance_travelled} {self.unit}, boat type: {self.boat_type}"

water_car = Carboatvehicle("4 cylinder engine")
water_car.travel(land_distance=50, water_distance=10)
print(water_car)
