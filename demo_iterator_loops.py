import sys

heroes = ['JFK', 'marie antoinette', 'm.jackson', 'ozzie', 'pele', 'malcom X', 'kobe', 'diana']

for idx, name in enumerate(heroes):
    heroes[idx] = name.title()

print("Heroes =", heroes)

try:
    sys.exit(0)
except SystemExit:
    print("Quitting..")
