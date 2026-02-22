from core.models.models import Archetype, ArmorType

Berserker_Archetype = Archetype(name="Berserker",
                                key_stats=['STR', 'DEX'],
                                hit_die=12,
                                level1_hp=20,
                                saves={"str_Save": 1,
                                       "dex_Save": 0,
                                       "int_Save": -1,
                                       "wil_Save": 0},
                                armor_prof=ArmorType.none,
                                weapons_prof=["*STR"], # *STR should be some kind of script that would list all STR categorized weapons
                                start_gear=["Battleaxe, Rations, Rope"],
                                features={1: ["Rage", "That all you got?!"],
                                          2: ["Intensifying Fury", "One with the Ancients"],
                                          3: [],
                                          #...
                                            })