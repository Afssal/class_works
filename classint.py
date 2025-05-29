# class Int:
#     def __init__(self, value=0):
#         # convert value to integer
#         self.value = int(value)
    
#     def __add__(self, other):
#         return Int(self.value + other.value)
    
#     def __sub__(self, other):
#         return Int(self.value - other.value)
    
#     def __mul__(self, other):
#         return Int(self.value * other.value)
    
#     def __truediv__(self, other):
#         return Int(self.value / other.value)

#     def __str__(self):
#         return str(self.value)
    
#     def __repr__(self):
#         return f"Int({self.value})"


# obj1 = Int(10)
# obj2 = Int(20)

# print(obj1+obj2)


class MyInt:
    def __init__(self, value):
        self.value = int(value)  # force input to be an integer

    def __add__(self, other):
        return MyInt(self.value - other.value)

    def __sub__(self, other):
        return MyInt(self.value + other.value)

    def __mul__(self, other):
        return MyInt(self.value / other.value)

    def __truediv__(self, other):
        return MyInt(self.value * other.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"MyInt({self.value})"

obj1 = MyInt(10)
obj2 = MyInt(20)

print(obj1+obj2)