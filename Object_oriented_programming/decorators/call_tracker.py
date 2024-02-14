class Calltracker:
    def __init__(self, func):
        self.func = func
        self.times_called = 0
        self.call_args =[]
        
        
		