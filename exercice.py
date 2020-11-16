"""
Chapitre 11.1
"""


import math
from inspect import *

from game import *


def main():
	wpn1 = Weapon("Nashor's Tooth", 40, 70)
	unarmed = Weapon.make_unarmed()
	Garosh = Character("Garosh", 200, 150, 70, 69)
	Garosh.weapon = Weapon("YOUR MOM", 69, 69)
	print(Garosh)
	# c1 = Character("Äpik", 200, 150, 70, 70)
	# c2 = Character("Gämmor", 250, 100, 120, 60)
	#
	# c1.weapon = Weapon("BFG", 100, 69)
	# c2.weapon = Weapon("Deku Stick", 120, 1)
	#
	# turns = run_battle(c1, c2)
	# print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

