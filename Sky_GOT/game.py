"""
    GOT - Game of Tanks for Sky employees
"""
import sys
from Sky_GOT.app.tank import Tank


# import tank

def main():
    # Created/Instantiated 3 Tank objects
    sage_tank = Tank("German", "Tiger")
    arash_tank = Tank("American", "Sherman")
    ben_tank = Tank("British", "Churchill")

    # And the game begins..
    sage_tank.accel(63)
    arash_tank.accel(29)

    ben_tank.rotate_left(289)
    ben_tank.accel(31)
    ben_tank.shoot()

    # And success..
    sage_tank.take_damage(59)
    arash_tank.take_damage(22)

    # And now for some VISUALS!
    print(f"Health of Sage's Tank is {sage_tank._health}")

    print(f"Health of Sage's and Arash's Tanks: {sage_tank + arash_tank}")

    # Example of GETTER and SETTER methods..
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Sage has received a health boost
    # sage_tank._health = 100 # POOR CODE - Variable is PRIVATE!
    # print(f"New health of Sage's tank: {sage_tank._health}")
    sage_tank.set_health(101)  # Good - using a SETTER method
    print(f"New health of Sage's tank: {sage_tank.get_health()}")  # Good - GETTER method



    return None

    # Some SPECIAL methods..
    # Example of OPERATOR OVERLOADING
    def __add__(self, other):
        return self._health + other._health


# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)