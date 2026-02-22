from functions.dice_roller import roll_XdY, roll_XdY_eZ

REPETITIONS = 100000 # 100.000 | 100k

def Monte_Carlo_eZ(x, y):
    r = REPETITIONS
    return (sum((roll_XdY_eZ(x, y, y) for _ in range(r)))/r)

def Monte_Carlo(x, y):
    r = REPETITIONS
    return (sum((roll_XdY(x, y) for _ in range(r)))/r)

print("Results:")
for i in range(2, 21, 2):
    print(f"1d{i}  --  {Monte_Carlo_eZ(1, i)}\n1d{i}eZ --  {Monte_Carlo_eZ(1, i)}")