Array = []

def create_array():
    global Array
    Array = [0] * 10

def insert_value(index, value):
    if index < len(Array):
        Array[index] = value
    else:
        print("Index out of bounds")
    
print("Creating array...")
create_array()
print("Inserting values...")
insert_value(0, 5)
insert_value(1, 10)
