# dinosaurs question
#
# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
# (normal code)
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
#
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

import math


name_dsr = {}


class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.leg_len = None
        self.diet = None
        self.stride_len = None
        self.stance = None

    def speed(self):
        return ((self.stride_len / self.leg_len) - 1) * math.sqrt(self.leg_len * 9.8)

    def is_valid(self):
        if self.leg_len is None or self.diet is None or self.stride_len is None or self.stance is None:
            return False
        return True

    def __lt__(self, other):
        return self.speed() < other.speed()


with open('dataset1.csv', 'r') as f:
    for line in f.readlines()[1:]:
        name, length, diet = line.split(',')
        name, length, diet = name.lower().strip(), float(length), diet.lower().strip()

        # setup
        name_dsr[name] = Dinosaur(name)
        name_dsr[name].leg_len = length
        name_dsr[name].diet = diet


with open('dataset2.csv', 'r') as f:
    for line in f.readlines()[1:]:
        name, length, stc = line.split(',')
        name, length, stc = name.lower().strip(), float(length), stc.lower().strip()

        # setup
        if name not in name_dsr:
            continue
        name_dsr[name].stride_len = length
        name_dsr[name].stance = stc


dsrs = []
for _, dsr in name_dsr.items():
    if dsr.stance == 'bipedal' and dsr.is_valid():
        dsrs.append(dsr)

dsrs.sort()
for dsr in dsrs:
    print(dsr.name)
