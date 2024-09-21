class Laptop:
    def __init__ (self, brand ,memory ,  battery_life ,size , storage, processor ):
        self.brand = brand
        self.memory = memory
        self.battery_life = battery_life
        self.size =size
        self.storage = storage
        self.processor = processor

    def laptop_details(self):
        return f" The brand is{self.brand} the memory {self.memory} , battery {self.battery_life}, the size is {self.size}, the storage {self.storage} , and processor {self.processor}"

# my_laptop = Laptop( "LENOVO""9gb", "100", "15.6 inches", "wide", "windows 12")
# print(my_laptop.laptop_details())

class myLaptop:
    def __init__ (self, brand ,memory ,  battery_life ,size , storage, processor, screen_quality ):
        self.brand = brand
        self.memory = memory
        self.battery_life = battery_life
        self.size =size
        self.storage = storage
        self.processor = processor
        self.screen_quality = screen_quality

    def laptop_details(self):
        return f" The brand is {self.brand} , the memory {self.memory} , battery {self.battery_life}, the size is {self.size}, the storage is {self.storage} , and processor {self.processor} with screen quality of{self.screen_quality}"

mylaptop = myLaptop("LENOVO", "9gb", "100", "15.6 inches", "wide", "windows 12","high resolution")
print(mylaptop.laptop_details())