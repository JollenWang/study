#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

from class_car import *

class Battery():
    def __init__(self, capability=70):
        self.capability = capability

    def get_capability(self):
        return self.capability

class ElectricCar(car):
    def __init__(self, year, brand, model):
        super().__init__(year, brand, model)
        self.battery = Battery()

    def battery_status(self):
        print("Battery capability is %d KWh" %self.battery.get_capability())

if __name__ == "__main__":
    my_car = ElectricCar(2016, "Tesla", "Model S")
    my_car.tell_info()
    my_car.battery_status()

