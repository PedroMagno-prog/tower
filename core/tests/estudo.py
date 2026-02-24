"""
TESTS with GEM to learn the function
# Usage example with scipy
x = [1, 50, 100] # FLOOR
y = [80, 55, 10] # WEIGHT defined (balance)

# Create the interpolating polynomial function
poly_test = lagrange(x, y) # poly is LITERALLY the function?

# Estimate a value
print(poly_test(50)) # poly(90) = f(x)
print(poly_test)
"""
"""
Conclusion:
    poly has surgical precision, but has a margin of error around 0.000 000 000 000 23

"""
import random
from collections import Counter

# --- 1. GENERAL LOOT SYSTEM CONFIGURATION ---
# Adjust these values to balance your game

# Rarity names. "Common" is special.
COMMON_RARITY_NAME = "Common"

# The "extremes" of your game
MIN_FLOOR = 1
MID_FLOOR = 50
MAX_FLOOR = 100

# 🧠 ANCHOR A: Base loot weights on Floor 1 (Early Game)
WEIGHTS_FLOOR_1 = {
    "Common": 80,
    "Uncommon": 15,
    "Rare": 4,
    "Epic": 0.9,
    "Legendary": 0.1
}
# 🧠 ANCHOR B: Base loot weights on Floor 50 (Mid-Game)
# Note how "Uncommon" rises quickly here, and declines later
WEIGHTS_FLOOR_50 = {
    "Common": 55,
    "Uncommon": 30,
    "Rare": 10,
    "Epic": 4,
    "Legendary": 1
}

# 🧠 ANCHOR C: Base loot weights on Floor 100 (End Game)
# Note how "Common" here is rarer than "Uncommon"
WEIGHTS_FLOOR_100 = {
    "Common": 10,
    "Uncommon": 20,
    "Rare": 40,
    "Epic": 20,
    "Legendary": 10
}

# ⚙️ DIFFICULTY MODIFIERS (0% to 100%)
# Maximum penalty "Common" can suffer with 100% difficulty
# (0.5 = 50% weight reduction)
# In this case I changed to 1.0 to be a TOTAL reduction at difficulty 100. There are no common items in
MAX_COMMON_PENALTY = 0.5

# Maximum bonus rare items can receive with 100% difficulty
# (1.0 = 100% bonus, meaning double the weight)
MAX_RARE_BONUS = 1.0


def lerp(a: float, b: float, t: float) -> float:
    # Linear Interpolation: Calculates a point between 'a' and 'b' based on 't'.
    return a + (b - a) * t
# Floor 50:
# 80 + (10-80) * 50
# 80 + (10-80) * 1


def calculate_base_weights(floor: int) -> dict:

     # STEP 1: Calculate base loot weights for the current floor
     # using linear interpolation between Floor 1 and Floor 100.

    # Ensures current floor is within limits
    floor = max(MIN_FLOOR, min(floor, MAX_FLOOR))

    # Calculate player floor (0.0 for Floor 1, 1.0 for Floor 100)
    floor = (floor - MIN_FLOOR) / (MAX_FLOOR - MIN_FLOOR)
    print(f"floor: {floor}")
    base_weights = {}

    # Iterate through all rarities defined in Anchor A
    for rarity in WEIGHTS_FLOOR_1.keys():
        weight_start = WEIGHTS_FLOOR_1[rarity]
        weight_end = WEIGHTS_FLOOR_100[rarity]

        # Calculate interpolated weight
        calculated_weight = lerp(weight_start, weight_end, floor)
        base_weights[rarity] = calculated_weight
    print(f"base_weights {base_weights}")
    return base_weights


def apply_difficulty_modifier(base_weights: dict, difficulty_percent: float) -> dict:

    # STEP 2: Apply difficulty modifier to base weights.
    # Decrease "Common" and increase all others.

    # Convert difficulty (ex: 80%) to a factor (ex: 0.8)
    difficulty_mod = max(0.0, min(difficulty_percent / 100.0, 1.0))

    print(f"difficulty_mod {difficulty_percent}")
    print(f"difficulty_mod {difficulty_mod}")

    final_weights = {}
    for rarity, base_weight in base_weights.items():
        if rarity == COMMON_RARITY_NAME:
            # Apply penalty to common item
            penalty_factor = MAX_COMMON_PENALTY * difficulty_mod
            final_weight = base_weight * (1.0 - penalty_factor)
        else:
            # Apply bonus to all other rarities
            bonus_factor = MAX_RARE_BONUS * difficulty_mod
            final_weight = base_weight * (1.0 + bonus_factor)

        # Ensure weight is never zero or negative
        print(f"final_wight: {final_weight}")
        final_weights[rarity] = max(0.01, final_weight)
    print(f"final_weights {final_weights}")
    return final_weights


def get_loot_rarity(final_weights: dict) -> str:

    # STEP 3: Perform RNG roll based on final weights.
    # Returns the name of the drawn rarity.

    # Extract rarities and their corresponding weights
    rarities = list(final_weights.keys())
    weights = list(final_weights.values())
    # random.choices does the weighted selection for us
    # Returns a list of 1 item, so we take [0]
    chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]
    return chosen_rarity

# --- 3. EXECUTION AND SIMULATION ---

def main_gem():
    # Main function to demonstrate and test the system.

    # --- SIMULATION PARAMETERS ---
    NUM_ROLLS = 50000  # Simulate 50,000 chest openings
    # -------------------------------

    floor = int(input("What floor are the players on? --> "))
    difficulty = int(input("What was the difficulty? --> "))

    print(f"--- 🎲 LOOT SIMULATION ---")
    print(f"Floor: {floor} | Difficulty: {difficulty}%\n")

    # STEP 1: Calculate base weights just for the Floor
    base_weights = calculate_base_weights(floor)
    print("--- Base Weights (Floor only) ---")
    for r, w in base_weights.items():
        print(f"{r:>9}: {w:.2f}")
    print("-" * 35)

    # STEP 2: Apply difficulty modifier
    final_weights = apply_difficulty_modifier(base_weights, difficulty)
    print(f"--- Final Weights (Floor + Difficulty {difficulty}%) ---")
    for r, w in final_weights.items():
        print(f"{r:>9}: {w:.2f}")
    print("-" * 35)

    # STEP 3: Simulate opening multiple chests
    print(f"📈 Simulating {NUM_ROLLS} chest openings...")
    loot_results = []
    for _ in range(NUM_ROLLS):
        rarity = get_loot_rarity(final_weights)
        loot_results.append(rarity)

    # Count and display results
    loot_counts = Counter(loot_results)

    # Sort by original rarity order for better visualization
    print("\n--- SIMULATION RESULT ---")
    total_rolls = sum(loot_counts.values())

    for rarity in WEIGHTS_FLOOR_1.keys():
        count = loot_counts[rarity]
        percentage = (count / total_rolls) * 100
        print(f"{rarity:>9}: {count} rolls ({percentage:.2f}%)")

if __name__ == '__main__':
    main_gem()