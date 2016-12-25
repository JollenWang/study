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

if __name__ == "__main__":
    mine = car(2014, "Toyota", "Camry 2.0S")
    mine.tell_info()
    mine.update_miles(40000)
    mine.tell_info()
