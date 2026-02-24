from core.models.models import Archetype, ArmorType

Berserker_Archetype = Archetype(
    name="Berserker",
    key_stats=['STR', 'DEX'],
    hit_die=12,
    level1_hp=20,
    saves={
        "str_Save": 1,
        "dex_Save": 0,
        "int_Save": -1,
        "wil_Save": 0
    },
    armor_prof=ArmorType.none,
    weapons_prof=["all STR weapons"],
    start_gear=["Battleaxe", "Rations (meat)", "Rope (50 ft.)"],
    features={
        1: ["Rage", "That all you got?!", "Your Rage Ends..."],
        2: ["Intensifying Fury", "One with the Ancients"],
        3: ["Subclass", "Bloodlust"],
        4: ["Enduring Rage", "Key Stat Increase", "Savage Arsenal", "Wrath & Ruin"],
        5: ["Rage (2)", "Secondary Stat Increase"],
        6: ["Savage Arsenal (2)", "Intensifying Fury (2)"],
        7: ["Subclass"],
        8: ["Savage Arsenal (3)", "Key Stat Increase"],
        9: ["Intensifying Fury (3)", "Secondary Stat Increase"],
        10: ["Savage Arsenal (4)"],
        11: ["Subclass"],
        12: ["Savage Arsenal (5)", "Key Stat Increase"],
        13: ["Intensifying Fury (4)", "Secondary Stat Increase"],
        14: ["Savage Arsenal (6)"],
        15: ["Subclass"],
        16: ["Savage Arsenal (7)", "Key Stat Increase"],
        17: ["Intensifying Fury (5)", "Secondary Stat Increase"],
        18: ["DEEP RAGE"],
        19: ["Epic Boon"],
        20: ["BOUNDLESS RAGE"]
    }
)

Cheat_Archetype = Archetype(
    name="The Cheat",
    key_stats=['DEX', 'INT'],
    hit_die=6,
    level1_hp=10,
    saves={
        "str_Save": 0,
        "dex_Save": 1,
        "int_Save": 0,
        "wil_Save": -1
    },
    armor_prof=ArmorType.leather,
    weapons_prof=["*DEX"],
    start_gear=["2 Daggers", "Sling", "Cheap Hides", "Chalk"],
    features={
        1: ["Sneak Attack", "Vicious Opportunist"],
        2: ["Cheat"],
        3: ["Subclass", "Sneak Attack (2)", "Thieves' Cant"],
        4: ["Key Stat Increase", "Underhanded Ability", "Trade Secrets"],
        5: ["Twist the Blade", "Quick Read", "Secondary Stat Increase"],
        6: ["Underhanded Ability (2)"],
        7: ["THAT'S Not What Happened!", "Subclass", "Sneak Attack (3)"],
        8: ["Underhanded Ability (3)", "Key Stat Increase"],
        9: ["Sneak Attack (4)", "Secondary Stat Increase"],
        10: ["Underhanded Ability (4)"],
        11: ["Subclass", "Sneak Attack (5)"],
        12: ["Underhanded Ability (5)", "Key Stat Increase"],
        13: ["Twist the Blade (2)", "Secondary Stat Increase"],
        14: ["Underhanded Ability (6)"],
        15: ["Subclass", "Sneak Attack (6)"],
        16: ["Underhanded Ability (7)", "Key Stat Increase"],
        17: ["Sneak Attack (7)", "Secondary Stat Increase"],
        18: ["Underhanded Ability (8)"],
        19: ["Epic Boon"],
        20: ["Supreme Execution"]
    }
)

Commander_Archetype = Archetype(
    name="Commander",
    key_stats=['STR', 'INT'],
    hit_die=10,
    level1_hp=17,
    saves={
        "str_Save": 1,
        "dex_Save": -1,
        "int_Save": 0,
        "wil_Save": 0
    },
    armor_prof=ArmorType.mail,
    weapons_prof=["All Martial Weapons"],
    start_gear=["Hand Axe", "Javelins (4)", "Rusty Mail"],
    features={
        1: ["Coordinated Strike!"],
        2: ["Commander's Orders", "Field Medic"],
        3: ["Subclass"],
        4: ["Fit for Any Battlefield", "Key Stat Increase", "Rigorous Training"],
        5: ["Master Commander", "Combat Tactics", "Secondary Stat Increase"],
        6: ["Fit for Any Battlefield (2)", "Weapon Mastery"],
        7: ["Subclass"],
        8: ["Fit for Any Battlefield (3)", "Key Stat Increase"],
        9: ["Master Commander (2)", "Combat Tactics (2)", "Secondary Stat Increase"],
        10: ["Fit for Any Battlefield (4)", "Weapon Mastery (2)"],
        11: ["Subclass"],
        12: ["Fit for Any Battlefield (5)", "Key Stat Increase"],
        13: ["Master Commander (3)", "Combat Tactics (3)", "Secondary Stat Increase"],
        14: ["Weapon Mastery (3)"],
        15: ["Subclass"],
        16: ["Fit for Any Battlefield (6)", "Key Stat Increase"],
        17: ["Master Commander (4)", "Combat Tactics (4)", "Secondary Stat Increase"],
        18: ["Unparalleled Tactics"],
        19: ["Epic Boon"],
        20: ["Captain of Legions"]
    }
)

Hunter_Archetype = Archetype(
    name="Hunter",
    key_stats=['DEX', 'WIL'],
    hit_die=8,
    level1_hp=13,
    saves={
        "str_Save": 0,
        "dex_Save": 1,
        "int_Save": -1,
        "wil_Save": 0
    },
    armor_prof=ArmorType.leather,
    weapons_prof=["*DEX"],
    start_gear=["Shortbow", "Cheap Hides", "Dagger", "Hunting Trap"],
    features={
        1: ["Hunter's Mark", "Forager"],
        2: ["Thrill of the Hunt", "Roll & Strike", "Remember the Wild"],
        3: ["Subclass", "Tracker's Intuition"],
        4: ["Thrill of the Hunt (2)", "Key Stat Increase", "Explorer of the Wilds"],
        5: ["Hunter's Resolve"],
        6: ["Final Takedown", "Secondary Stat Increase", "Versatile Bowmaster", "Thrill of the Hunt (3)"],
        7: ["Subclass"],
        8: ["Thrill of the Hunt (4)", "Key Stat Increase"],
        9: ["No Escape", "Secondary Stat Increase"],
        10: ["Veteran Stalker", "Keen Eye, Steady Hand"],
        11: ["Subclass"],
        12: ["Thrill of the Hunt (5)", "Key Stat Increase"],
        13: ["Keen Sight", "Secondary Stat Increase"],
        14: ["Thrill of the Hunt (6)"],
        15: ["Subclass"],
        16: ["Key Stat Increase"],
        17: ["Peerless Hunter", "Secondary Stat Increase"],
        18: ["Wild Endurance"],
        19: ["Epic Boon"],
        20: ["Nemesis"]
    }
)

Mage_Archetype = Archetype(
    name="Mage",
    key_stats=['INT', 'WIL'],
    hit_die=6,
    level1_hp=10,
    saves={
        "str_Save": -1,
        "dex_Save": 0,
        "int_Save": 1,
        "wil_Save": 0
    },
    armor_prof=ArmorType.cloth,
    weapons_prof=["Blades", "Staves", "Wands"],
    start_gear=["Adventurer's Garb", "Staff", "Soap"],
    features={
        1: ["Elemental Spellcasting"],
        2: ["Mana and Unlock Tier 1 Spells", "Talented Researcher"],
        3: ["Subclass", "Elemental Mastery", "Study!"],
        4: ["Spellshaper", "Tier 2 Spells", "Key Stat Increase"],
        5: ["Elemental Surge", "Secondary Stat Increase", "Upgraded Cantrips"],
        6: ["Tier 3 Spells", "Elemental Mastery (2)"],
        7: ["Subclass"],
        8: ["Tier 4 Spells", "Key Stat Increase"],
        9: ["Spellshaper (2)", "Secondary Stat Increase"],
        10: ["Elemental Surge (2)", "Tier 5 Spells", "Upgraded Cantrips"],
        11: ["Subclass"],
        12: ["Tier 6 Spells", "Key Stat Increase"],
        13: ["Spellshaper (3)", "Secondary Stat Increase"],
        14: ["Tier 7 Spells", "Elemental Mastery (3)"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Tier 8 Spells", "Key Stat Increase"],
        17: ["Elemental Surge (3)", "Secondary Stat Increase"],
        18: ["Tier 9 Spells"],
        19: ["Epic Boon"],
        20: ["Archmage", "Upgraded Cantrips"]
    }
)

Oathsworn_Archetype = Archetype(
    name="Oathsworn",
    key_stats=['STR', 'WIL'],
    hit_die=10,
    level1_hp=17,
    saves={
        "str_Save": 1,
        "dex_Save": -1,
        "int_Save": 0,
        "wil_Save": 0
    },
    armor_prof=ArmorType.plate,
    weapons_prof=["STR Weapons"],
    start_gear=["Mace", "Rusty Mail", "Wooden Buckler", "Manacles"],
    features={
        1: ["Radiant Judgment", "Lay on Hands"],
        2: ["Mana and Radiant Spellcasting", "Zealot", "Paragon of Virtue"],
        3: ["Subclass", "Radiant Judgment (2)", "Sacred Decree", "Serve Selflessly"],
        4: ["My Life, for My Friends", "Tier 2 Spells", "Key Stat Increase"],
        5: ["Radiant Judgment (3)", "Upgraded Cantrips", "Secondary Stat Increase"],
        6: ["Tier 3 Spells", "Sacred Decree (2)"],
        7: ["Subclass", "Master of Radiance"],
        8: ["Tier 4 Spells", "Radiant Judgment (4)", "Key Stat Increase"],
        9: ["Sacred Decree (3)", "Secondary Stat Increase"],
        10: ["Tier 5 Spells", "Upgraded Cantrips", "Radiant Judgment (5)"],
        11: ["Subclass", "Master of Radiance (2)"],
        12: ["Sacred Decree (4)", "Key Stat Increase"],
        13: ["Tier 6 Spells", "Secondary Stat Increase"],
        14: ["Sacred Decree (5)", "Radiant Judgment (6)"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Sacred Decree (6)", "Key Stat Increase"],
        17: ["Tier 7 Spells", "Secondary Stat Increase"],
        18: ["Unending Judgment"],
        19: ["Epic Boon"],
        20: ["Glorious Paragon", "Upgraded Cantrips"]
    }
)

Shadowmancer_Archetype = Archetype(
    name="Shadowmancer",
    key_stats=['INT', 'DEX'],
    hit_die=8,
    level1_hp=13,
    saves={
        "str_Save": 0,
        "dex_Save": 0,
        "int_Save": 1,
        "wil_Save": -1
    },
    armor_prof=ArmorType.cloth,
    weapons_prof=["Blades", "Wands"],
    start_gear=["Adventurer's Garb", "Sickle", "Shovel"],
    features={
        1: ["Conduit of Shadow"],
        2: ["Master of Darkness", "Pilfered Power"],
        3: ["THE PACT IS SEALED", "Supplicate"],
        4: ["Key Stat Increase", "A Gift from the Master"],
        5: ["Tier 2 Spells", "Upgraded Cantrips", "Secondary Stat Increase"],
        6: ["A Gift from the Master (2)", "Shadowmastery"],
        7: ["Subclass", "Tier 3 Spells"],
        8: ["Key Stat Increase", "Lesser Invocation", "Shadowmastery (2)"],
        9: ["A Gift from the Master (3)", "Secondary Stat Increase"],
        10: ["Tier 4 Spells", "Upgraded Cantrips"],
        11: ["Subclass", "Lesser Invocation (2)"],
        12: ["Greedy Pact", "Key Stat Increase"],
        13: ["Tier 5 Spells", "Secondary Stat Increase"],
        14: ["A Gift from the Master (4)", "Shadowmastery (3)"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Tier 6 Spells", "Key Stat Increase"],
        17: ["Dire Shadows", "Secondary Stat Increase"],
        18: ["A Gift from the Master (5)"],
        19: ["Epic Boon", "Tier 7 Spells"],
        20: ["Eldritch Usurper", "Upgraded Cantrips"]
    }
)

Shepherd_Archetype = Archetype(
    name="Shepherd",
    key_stats=['WIL', 'STR'],
    hit_die=10,
    level1_hp=17,
    saves={
        "str_Save": 0,
        "dex_Save": -1,
        "int_Save": 0,
        "wil_Save": 1
    },
    armor_prof=ArmorType.mail,
    weapons_prof=["STR Weapons", "Wands"],
    start_gear=["Rusty Mail", "Mace", "Wooden Buckler", "Bell"],
    features={
        1: ["Keeper of Life & Death", "Searing Light"],
        2: ["Mana and Unlock Tier 1 Spells", "Lifebinding Spirit"],
        3: ["Subclass", "Master of Twilight"],
        4: ["Tier 2 Spells", "Key Stat Increase"],
        5: ["Secondary Stat Increase", "Upgraded Cantrips", "Sacred Grace", "Serve"],
        6: ["Tier 3 Spells", "Master of Twilight (2)"],
        7: ["Subclass"],
        8: ["Tier 4 Spells", "Key Stat Increase"],
        9: ["Sacred Grace (2)", "Secondary Stat Increase"],
        10: ["Tier 5 Spells", "Upgraded Cantrips"],
        11: ["Subclass", "Master of Twilight (3)"],
        12: ["Tier 6 Spells", "Key Stat Increase"],
        13: ["Sacred Grace (3)", "Secondary Stat Increase"],
        14: ["Tier 7 Spells"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Tier 8 Spells", "Key Stat Increase"],
        17: ["Revitalizing Blessing", "Secondary Stat Increase"],
        18: ["Tier 9 Spells"],
        19: ["Epic Boon"],
        20: ["Twilight Sage", "Upgraded Cantrips"]
    }
)

Songweaver_Archetype = Archetype(
    name="Songweaver",
    key_stats=['WIL', 'INT'],
    hit_die=8,
    level1_hp=13,
    saves={
        "str_Save": -1,
        "dex_Save": 0,
        "int_Save": 0,
        "wil_Save": 1
    },
    armor_prof=ArmorType.leather,
    weapons_prof=["*DEX", "Wands"],
    start_gear=["Adventurer's Garb", "Instrument", "Dagger", "Mirror"],
    features={
        1: ["Wind Spellcasting", "Vicious Mockery", "Songweaver's Inspiration"],
        2: ["Mana and Unlock Tier 1 Spells", "Jack of All Trades", "Song of Rest"],
        3: ["Subclass", "Quick Wit", "Windbag"],
        4: ["Tier 2 Spells", "Key Stat Increase", "Lyrical Weaponry", "Perform!"],
        5: ["A 'People' Person", "Upgraded Cantrips", "Secondary Stat Increase"],
        6: ["Tier 3 Spells", "Windbag (2)"],
        7: ["Subclass"],
        8: ["Tier 4 Spells", "Key Stat Increase"],
        9: ["Lyrical Weaponry (2)", "Secondary Stat Increase"],
        10: ["Tier 5 Spells", "Upgraded Cantrips"],
        11: ["Subclass"],
        12: ["Tier 6 Spells", "Key Stat Increase"],
        13: ["Lyrical Weaponry (3)", "Secondary Stat Increase"],
        14: ["Tier 7 Spells", "Windbag (3)"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Tier 8 Spells", "Key Stat Increase"],
        17: ["Lyrical Weaponry (4)", "Secondary Stat Increase"],
        18: ["Tier 9 Spells"],
        19: ["Epic Boon"],
        20: ["I'm So Famous!", "Upgraded Cantrips"]
    }
)

Stormshifter_Archetype = Archetype(
    name="Stormshifter",
    key_stats=['WIL', 'DEX'],
    hit_die=8,
    level1_hp=13,
    saves={
        "str_Save": -1,
        "dex_Save": 0,
        "int_Save": 0,
        "wil_Save": 1
    },
    armor_prof=ArmorType.leather,
    weapons_prof=["Staves", "Wands"],
    start_gear=["Cheap Hides", "Staff", "Strange Plant"],
    features={
        1: ["Master of Storms", "Beastshift"],
        2: ["Direbeast Form", "Mana and Unlock Tier 1 Spells"],
        3: ["Subclass", "Direbeast Form (2)"],
        4: ["Tier 2 Spells", "Key Stat Increase", "Stormcaller", "Be Wild"],
        5: ["Direbeast Form (3)", "Upgraded Cantrips", "Secondary Stat Increase"],
        6: ["Chimeric Boon", "Expert Shifter", "Tier 3 Spells"],
        7: ["Subclass", "Stormcaller (2)"],
        8: ["Tier 4 Spells", "Key Stat Increase", "Stormborn"],
        9: ["Chimeric Boon (2)", "Expert Shifter (2)", "Secondary Stat Increase"],
        10: ["Tier 5 Spells", "Upgraded Cantrips"],
        11: ["Subclass"],
        12: ["Tier 6 Spells", "Key Stat Increase", "Chimeric Boon (3)", "Expert Shifter (3)"],
        13: ["Secondary Stat Increase", "Stormborn (2)"],
        14: ["Tier 7 Spells"],
        15: ["Subclass", "Upgraded Cantrips"],
        16: ["Tier 8 Spells", "Key Stat Increase"],
        17: ["Chimeric Boon (4)", "Secondary Stat Increase"],
        18: ["Tier 9 Spells"],
        19: ["Epic Boon"],
        20: ["Archdruid", "Upgraded Cantrips"]
    }
)

Zephyr_Archetype = Archetype(
    name="Zephyr",
    key_stats=['DEX', 'STR'],
    hit_die=8,
    level1_hp=13,
    saves={
        "str_Save": 0,
        "dex_Save": 1,
        "int_Save": -1,
        "wil_Save": 0
    },
    armor_prof=ArmorType.none,
    weapons_prof=["Melee"],
    start_gear=["Staff", "Traveling Robes & Sandals"],
    features={
        1: ["Iron Defense", "Swift Fists"],
        2: ["Swift Feet", "Burst of Speed"],
        3: ["Subclass", "Kinetic Momentum", "Ethereal Projection"],
        4: ["Unyielding Resolve", "Key Stat Increase", "Martial Master", "Focus"],
        5: ["Reverberating Strikes", "Secondary Stat Increase"],
        6: ["Martial Master (2)", "Infuse Strength"],
        7: ["Subclass"],
        8: ["Martial Master (3)", "Key Stat Increase"],
        9: ["Swift Feet (2)", "Secondary Stat Increase"],
        10: ["Martial Master (4)", "Unyielding Resolve (2)"],
        11: ["Subclass"],
        12: ["Martial Master (5)", "Key Stat Increase"],
        13: ["Iron Defense (2)", "Secondary Stat Increase"],
        14: ["Martial Master (6)"],
        15: ["Subclass"],
        16: ["Martial Master (7)", "Key Stat Increase"],
        17: ["Unyielding Resolve (3)", "Secondary Stat Increase"],
        18: ["Martial Master (8)"],
        19: ["Epic Boon"],
        20: ["Windborne"]
    }
)


