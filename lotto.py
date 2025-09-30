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
    num= random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number =", num)

    print("lottery numbers =", lotto)