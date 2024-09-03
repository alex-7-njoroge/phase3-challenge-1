class Car:
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year = year
    def display_info(self):
        print(f'Make: {self.make}')
        print(f'Make: {self.model}')
        print(f'Make: {self.year}')
alex_car = Car('Volvo','SUV Luxury',2025 )
alex_car.display_info()