def add_four(func):
    def wrapper(*args, **kwargs):
        print("we are adding 4")
        result = func (*args, **kwargs)
        return result + 4
    return wrapper

def double(func):
    def wrapper(*args, **kwargs):
        print("we are doubling")
        result = func (*args, **kwargs)
        return result * 2
    return wrapper

@double
@add_four
def add(a,b):
    print (f"we are adding  {a} , {b}")
    return a + b  

print(add(1,3))



    
		
	

        
        