#*args =allows you to pass multiple non-key arguments
#**kwargs=allows you to pass multiple keyword arguments
#        *unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print (add(1,2,3,4,5,6))

def display_name(*names):
    for name in names:
        print(name, end=" ")
display_name("Mr.","Peter","Parker")

#kwargs
def print_address(**kwargs):
    for key,value in kwargs.items():
     print(f"{key}: {value}")  
print_address(street="123 Fake St.",
             apt="100",
              city="Detroit",
              state="MI",
              zip="54321")  
    
        




     