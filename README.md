# Tower RPG Manager (Core)

A comprehensive CLI tool designed for Tabletop RPG Game Masters and Designers. This project automates administrative tasks, handles complex probability calculations for loot generation, and manages game data persistence.

Built originally for the "Synergia/Tower" system, but adaptable for other d20-based systems.

## 📋 Features

### 🎲 Advanced Dice Roller (`dice_roller.py`)
A robust parsing engine capable of handling complex dice notations and modifiers:
- **Standard Rolls:** `XdY` (e.g., `4d6`).
- **Modifiers:** Drop Lowest (`dl`), Drop Highest (`dh`), and static bonuses (`+5`, `-2`).
- **Exploding Dice:** Mechanics where max-value rolls trigger re-rolls.
- **Complex Action Parsing:** The `read_action` function interprets complex strings like `2#3d12dl1e-5` (2 iterations of 3d12, drop lowest, exploding dice, with a -5 penalty).

### ⚔️ Encounter & Loot RNG (`rng.py`)
- **Procedural Generation:** Uses **Lagrange Interpolation (`scipy`)** to calculate loot rarity probabilities dynamically based on the current Dungeon Floor.
- **Encounter Balancing:** Adjusts difficulty based on party size and level.
- **Filtering:** Generates encounters based on Monster Families (e.g., Undead, Construct) within a specific XP/Difficulty budget.

### 📦 Data Persistence (`cadastro_db.py`)
- **JSON Database:** Lightweight storage for Monsters (`monstros.json`) and Loot (`loots.json`).
- **CLI Management:** Built-in menu to Create, Read, and Update game objects directly from the terminal without editing raw files.
- **Categorization:** Organizations by Tier (Minion, Normal, Legendary) and Family.

## 🛠️ Tech Stack

- **Python 3.x**
- **Scipy & Numpy:** Used for advanced probability curves and interpolation.
- **JSON:** Native Python library for data serialization.

## 🚀 Getting Started

### Prerequisites
You need Python installed. This project relies on scientific libraries for its RNG calculations.

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/PROJECT-NAME.git](https://github.com/YOUR-USERNAME/PROJECT-NAME.git)
   cd PROJECT-NAME
