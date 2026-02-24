from core.models.models import Character, Archetype, Ancestry, Stats, Skills, ArmorType, CharSize

Flecher = Character(
    name="Flecher",
    archetype=Archetype(
        name="Hunter",
        key_stats=["DEX", "WIL"],
        hit_die=8,
        level1_hp=13,
        saves={"str_Save": 0, "dex_Save": 1, "int_Save": -1, "wil_Save": 0},
        armor_prof=ArmorType.leather,
        weapons_prof=["*DEX"],
        start_gear=["Shortbow", "Cheap Hides", "Dagger", "Hunting Trap"],
        features={"1": ["Hunter's Mark", "Forager"]}
    ),
    ancestry=Ancestry(
        name="Human",
        size=CharSize.Medium,
        bonus=Ancestry.AncBonus()
    ),
    stats=Stats(
        STR=0,
        DEX=2,
        INT=-1,
        WIL=2
    ),
    skills=Skills(
        arcana=0,
        craft=0,
        examination=0,
        finesse=0,
        influence=0,
        insight=0,
        lore=0,
        might=0,
        naturecraft=0,
        perception=0,
        stealth=0
    ),
    armor=5,
    level=1,
    speed=6,
    # initiative=2,
    # hp_max=13,
    # hp=13,
    # hd_max=1,
    # hd=1,
    wounds_max=6,
    wounds=0,
    mana_max=0,
   # inv_slots=10
)