from Math import pi
class Vehicle:
    default_tire = "tire"
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        
    @classmethod
    def bicycle(cls,tires=None):
        if not tires:
            tries = [cls.default_tire, cls.default_tire]
        return cls(None, tires)
    
        
    @staticmethod
    def wheel_circumferece(radius):
        return 2 * radius
        
        
    