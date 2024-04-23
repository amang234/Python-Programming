class Mobile:
    def __init__(self, color, shape, size):
        self.color = color
        self.shape = shape
        self.size = size

    def get_details(self):
        return f"Color: {self.color}, Shape: {self.shape}, Size: {self.size}"


mobile1 = Mobile("black", "rectangular", "medium")
mobile2 = Mobile("white", "square", "small")

print("Mobile 1:",mobile1.get_details())
print("Mobile 2:",mobile2.get_details())