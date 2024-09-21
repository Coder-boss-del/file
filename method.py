class Car:
    def __init__(self, brand, model, year, color, tramission_type, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.tramission_type = tramission_type
        self.engine = engine
    
    def summary(self):
        return f"Your car brand is {self.brand},{self.model}, {self.year} ,{self.color} ,{self.tramission_type}, {self.engine}"
    
my_car = Car("Porshe", "amg", "2011", "gold", "manual", "v8")
print(my_car.summary())