#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

class car():
    def __init__(self, year, brand, model):
        self.year = year
        self.brand = brand
        self.model = model
        self.odo_miles = 0

    def tell_info(self):
        print("Car info: %d %s %s." %(self.year, self.brand, self.model))
        print("---->ODO_MILES: %d" %self.odo_miles)

    def update_miles(self, miles):
        self.odo_miles += miles

class electric_car(car):
    def __init__(self, year, brand, model, price):
        super().__init__(year, brand, model)
        self.price = price

    def tell_info(self):
        super().tell_info()
        print("The price is %d." %self.price)


if __name__ == "__main__":
    mine = electric_car(2016, "Tesla", "Model S", 800000)
    mine.tell_info()
    mine.update_miles(40000)
    mine.tell_info()
