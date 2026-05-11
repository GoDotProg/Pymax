Array = []

def create_array():
    global Array
    Array = [0] * 10
    print("Array created with 10 elements.")

def insert_value(index, value):
    if index < len(Array):
        Array[index] = value
        print(f"Value inserted at index {index}: {value}")
    else:
        print("Index out of bounds")
    
print("Creating array...")
create_array()
print("Inserting values...")
insert_value(0, 5)
insert_value(1, 10)
print("Final array:")
print(Array)
