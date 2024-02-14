from vehicle import Vehicle
class Car(Vehicle):
    default_tire = "tire"
    
    def __init__(self, engine, tires=None, distance_travelled=0, unit="miles"):
        super().__init__(distance_travelled, unit)
        if tires is None:
            tires = [self.default_tire] * 4
        self.tires = tires
        self.engine = engine
    
    def drive(self, distance):
        self.distance_travelled += distance

        
    