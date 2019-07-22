import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)
        
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        
        # calc body size
        try:
            size = body_whl.split('x')
            self.body_width = float(size[0])
            self.body_height = float(size[1])
            self.body_length = float(size[2])
        except:
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
    
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    # car_type; brand; passenger_seats_count; photo_file_name; body_whl; carrying; extra
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) 
        for row in reader:
            if len(row)==7:
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
    return car_list
    
# TEST
# for car in get_car_list('cars.csv'):
#     print(car)

