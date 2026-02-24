WHITE = '\033[29m'
BLACK = '\033[30m'
BLACKBACK = '\033[40m'
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'

RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

# --- Cyberpunk ---
"""
H1 = BOLD + PINK         # Impactful main title
H2 = BOLD + LIGHTCYAN    # Clear subtitles
H3 = LIGHTBLUE           # Secondary sections
H4 = PURPLE              # Technical notes
BODY = LIGHTGREY         # Readable text
FOOTER = DARKGREY + '\033[3m' # Italic and discreet
"""

# --- Elven Forest ---
"""
H1 = BOLD + GREEN        # Ancient Forest
H2 = BOLD + LIGHTCYAN    # Elven Magic / River
H3 = LIGHTGREEN          # Herbs and Items
H4 = PINK                # Rare Artifacts
BODY = LIGHTGREY         # Mist (Standard text)
FOOTER = DARKGREY        # Shadows
"""

# --- Dungeon Crawler (Blood and Iron) ---
"""
H1 = BOLD + RED          # Blood (Monster or Boss title)
H2 = BOLD + DARKGREY     # Iron/Stone (Environment)
H3 = LIGHTGREEN          # Poison/Alchemy (Status)
H4 = YELLOW              # Torch/Light (Hints or Exits)
BODY = LIGHTGREY         # Ashes (Room description)
FOOTER = '\033[41m' # Red background (Death or Imminent Danger)
"""

# --- The Royal Order ---
"""
H1 = BOLD + YELLOW       # Royal Gold (Quest Title)
H2 = BOLD + PURPLE       # Nobility/Magic (Location or important NPC)
H3 = ORANGE              # Bronze (Subsections or Items)
H4 = LIGHTRED            # Wax Seal (Alerts or Danger)
BODY = LIGHTGREY         # Parchment (Narration)
FOOTER = DARKGREY        # Chronicle Footer
"""

# --- The Old Man at the Bridge ---
H1 = BOLD + YELLOW       # Royal Gold (Quest Title)
H2 = BOLD + LIGHTCYAN    # Elven Magic / River
H3 = LIGHTGREEN          # Herbs and Items
H4 = PINK                # Rare Artifacts
HIGHLIGHT = BLACKBACK    # Important shit
BODY = WHITE             # (Standard text)
FOOTER = LIGHTGREY       # Shadows


# print(f"{H1}--- MY PROGRAM v1.0 ---{RESET}")
# print(f"{H2}Settings loaded{RESET}")
# print(f"{H3}Settings loaded{RESET}")
# print(f"{H4}Settings loaded{RESET}")
# print(f"{BODY}The system is operating normally.{RESET}")
# print(f"{FOOTER} Press CTRL+C to exit {RESET}")
#
# print()
#
# def print_h1(texto):
#     print(f"{H1}══ {texto.upper()} ══{RESET}")
#
# def print_caixa(texto):
#     print(f"{H3}┌────────────────────────────┐")
#     print(f"│ {BODY}{texto.center(26)}{H3} │")
#     print(f"└────────────────────────────┘{RESET}")
#
# # Usage example:
# print_h1("The Dragon's Awakening")
# print(f"{BODY}You enter a cold room...{RESET}")
# print_caixa("IRON SWORD FOUND")