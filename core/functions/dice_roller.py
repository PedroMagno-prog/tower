from random import randint

"""
Many functions were inspired by the Discord BOT rollem

4d6 -- sum of 4 6-sided dice
4#d6 -- 4 rolls of 1d6

4d6dl1 -- drop the lowest and remove from sum

4d6dh1  -- drop the highest and remove from sum 

6#4d6 -- 6 rolls of 4d6
"""

"""
Simulates rolling 'x' dice with 'y' sides.

Args:
    x (int): number of dice to be rolled.
    y (int): number of sides of each die.

Returns:
    list: A list of integers with the results of each die.
"""

def roll_XdY(x:int, y:int)-> list:
    return list((randint(1, y)) for _ in range(x))

# drop the A lowest result
def roll_XdYdlA(x:int, y:int, z:int)-> list:
    rolls_sort = sorted(roll_XdY(x, y))
    for _ in range(z):
        rolls_sort.pop(0)
    return rolls_sort

# drop A highest result
def roll_XdYdhA(x:int, y:int, z:int)-> list:
    rolls_sort = sorted(roll_XdY(x, y), reverse=True)
    for _ in range(z):
        rolls_sort.pop(0)
    return rolls_sort

# roll XdY exploding at Z and above
def roll_XdY_eZ(x, y, z):
    result = roll_XdY(x, y)
    sum_ = sum(result)
    if result[0] >= z:
        sum_ += roll_XdY_eZ(x, y, z)
    return sum_

# roll XdY, missing in an 1 and criting in the max value of the die
def roll_Nimble(x, y, vicious=False):
    roll = roll_XdY(x, y)
    sum_ = sum(roll)
    if roll[0] == y:
        print("Crit")
        if not vicious:
            sum_ += roll_XdY_eZ(1, y, y)
        else:
            sum_ += roll_XdY_eZ(2, y, y)
        pass
    elif roll[0] == 1:
        print("Miss")
        return 0
    return sum_

def roll_witcher_1d10(base=0):
    roll = roll_XdY(1, 10)
    base += roll[0]
    explode = roll_XdY_eZ(1, 10, 10)
    if roll[0] == 10:
        base += explode
    elif roll[0] == 1:
        base -= explode
    return base
    pass

#print(roll_Nimble(4, 4, True))
#print(roll_witcher_1d10(5))