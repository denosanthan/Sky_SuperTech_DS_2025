#! usr/bin/env python3
# Author: Deenesh
# Version: 1.0
# Description : This script will generate 6 UNIQUE random
# lottery numbers

"""
    Docstring:
"""

import random

lotto = () # Create Empty List

while len(lotto) < 6:
    lotto = lotto + (random.randint(1,10),)
    lotto.append(num)
    if num in lotto:
        print("Duplicate number =", num)
    else:
        lotto.append(num)

print("lottery numbers =", lotto)