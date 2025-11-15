#!/usr/bin/env python3

import os
import requests

# All items with their icon URLs
items = [
    # Base items
    {"name": "Iron", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/98/Iron_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Ghost", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f8/Ghost_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Dark", "icon": "https://static.wikia.nocookie.net/ballpit/images/6/63/Dark_Ball.png/revision/latest?cb=20251022183558"},
    {"name": "Charm", "icon": "https://static.wikia.nocookie.net/ballpit/images/0/0b/Charm_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Burn", "icon": "https://static.wikia.nocookie.net/ballpit/images/6/65/Burn_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Bleed", "icon": "https://static.wikia.nocookie.net/ballpit/images/a/a3/Bleed_Ball.png/revision/latest?cb=20251022183501"},
    {"name": "Sun", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/9c/Sun_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Brood Mother", "icon": "https://static.wikia.nocookie.net/ballpit/images/8/8d/Brood_Mother_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Cell", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/d0/Cell_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Earthquake", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/92/Earthquake_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Egg Sac", "icon": "https://static.wikia.nocookie.net/ballpit/images/6/67/Egg_Sac_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Freeze", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/c4/Freeze_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Laser (Horizontal)", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/7f/Laser_%28Horizontal%29_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Laser (Vertical)", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/c7/Laser_%28Vertical%29_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Light", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/4a/Light_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Lightning", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/41/Lightning_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Poison", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/41/Poison_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Vampire", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f5/Vampire_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Wind", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/77/Wind_Ball.png/revision/latest?cb=20251022183559"},
    {"name": "Bomb", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/7e/Bomb_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Incubus", "icon": "https://static.wikia.nocookie.net/ballpit/images/0/08/Incubus_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Succubus", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f0/Succubus_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Mosquito King", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/47/Mosquito_King_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Spider Queen", "icon": "https://static.wikia.nocookie.net/ballpit/images/6/69/Spider_Queen_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Vampire Lord", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/11/Vampire_Lord_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Baby Rattle", "icon": "https://static.wikia.nocookie.net/ballpit/images/e/ed/Baby_Rattle.png/revision/latest/scale-to-width-down/100?cb=20251024023811"},
    {"name": "War Horn", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/9c/War_Horn.png/revision/latest?cb=20251024025023"},
    {"name": "Reacher's Spear", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/c2/Reachers_Spear.png/revision/latest?cb=20251024023811"},
    {"name": "Deadeye's Amulet", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f8/Deadeyes_Amulet.png/revision/latest?cb=20251024023811"},
    {"name": "Wretched Onion", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f2/Wretched_Onion.png/revision/latest?cb=20251024023811"},
    {"name": "Breastplate", "icon": "https://static.wikia.nocookie.net/ballpit/images/2/2b/Breastplate.png/revision/latest?cb=20251024023811"},
    {"name": "Ghostly Corset", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/fb/Ghostly_Corset.png/revision/latest?cb=20251024023811"},
    {"name": "Ethereal Cloak", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/73/Ethereal_Cloak.png/revision/latest?cb=20251024023811"},
    {"name": "Vampiric Sword", "icon": "https://static.wikia.nocookie.net/ballpit/images/8/87/Vampiric_Sword.png/revision/latest?cb=20251024025023"},
    {"name": "Everflowing Goblet", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/7a/Everflowing_Goblet.png/revision/latest?cb=20251024023811"},
    {"name": "Spiked Collar", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/1d/Spiked_Collar.png/revision/latest?cb=20251024024938"},
    {"name": "Crown of Thorns", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/19/Crown_Of_Thorns.png/revision/latest?cb=20251024023811"},
    {"name": "Radiant Feather", "icon": "https://static.wikia.nocookie.net/ballpit/images/b/ba/Radiant_Feather.png/revision/latest?cb=20251024023811"},
    {"name": "Fleet Feet", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f3/Fleet_Feet.png/revision/latest?cb=20251024023811"},
    {"name": "Diamond Hilted Dagger", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/d6/Diamond_Hilted_Dagger.png/revision/latest?cb=20251024023811"},
    {"name": "Sapphire Hilted Dagger", "icon": "https://static.wikia.nocookie.net/ballpit/images/7/70/Sapphire_Hilted_Dagger.png/revision/latest?cb=20251024023811"},
    {"name": "Ruby Hilted Dagger", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/50/Ruby_Hilted_Dagger.png/revision/latest?cb=20251024023811"},
    {"name": "Emerald Hilted Dagger", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/51/Emerald_Hilted_Dagger.png/revision/latest?cb=20251024023811"},

    # Evolutions
    {"name": "Assassin", "icon": "https://static.wikia.nocookie.net/ballpit/images/b/bb/Assassin_Ball.png/revision/latest?cb=20251022191404"},
    {"name": "Berserk", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/18/Berserk_Ball.png/revision/latest?cb=20251023153247"},
    {"name": "Black Hole", "icon": "https://static.wikia.nocookie.net/ballpit/images/8/84/Black_Hole_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Blizzard", "icon": "https://static.wikia.nocookie.net/ballpit/images/a/ae/Blizzard_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Flash", "icon": "https://static.wikia.nocookie.net/ballpit/images/2/27/Flash_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Flicker", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/96/Flicker_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Freeze Ray", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/99/Freeze_Ray_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Frozen Flame", "icon": "https://static.wikia.nocookie.net/ballpit/images/2/2e/Frozen_Flame_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Glacier", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/50/Glacier_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Hemorrhage", "icon": "https://static.wikia.nocookie.net/ballpit/images/0/0d/Hemorrhage_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Holy Laser", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/14/Holy_Laser_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Inferno", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/15/Inferno_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Laser Beam", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/97/Laser_Beam_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Leech", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/59/Leech_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Lightning Rod", "icon": "https://static.wikia.nocookie.net/ballpit/images/3/31/Lightning_Rod_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Lovestruck", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/17/Lovestruck_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Maggot", "icon": "https://static.wikia.nocookie.net/ballpit/images/2/26/Maggot_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Magma", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f6/Magma_Ball.png/revision/latest?cb=20251023153248"},
    {"name": "Mosquito Swarm", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/c4/Mosquito_Swarm_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Noxious", "icon": "https://static.wikia.nocookie.net/ballpit/images/8/8c/Noxious_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Nuclear Bomb", "icon": "https://static.wikia.nocookie.net/ballpit/images/8/85/Nuclear_Bomb_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Overgrowth", "icon": "https://static.wikia.nocookie.net/ballpit/images/6/6c/Overgrowth_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Phantom", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/d3/Phantom_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Radiation Beam", "icon": "https://static.wikia.nocookie.net/ballpit/images/0/0a/Radiation_Beam_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Sacrifice", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/47/Sacrifice_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Sandstorm", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/96/Sandstorm_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Satan", "icon": "https://static.wikia.nocookie.net/ballpit/images/a/a2/Satan_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Shotgun", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/dc/Shotgun_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Soul Sucker", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/c6/Soul_Sucker_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Storm", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/48/Storm_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Swamp", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/12/Swamp_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Virus", "icon": "https://static.wikia.nocookie.net/ballpit/images/c/cd/Virus_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Voluptuous Egg Sac", "icon": "https://static.wikia.nocookie.net/ballpit/images/4/4f/Voluptuous_Egg_Sac_Ball.png/revision/latest?cb=20251023163048"},
    {"name": "Wraith", "icon": "https://static.wikia.nocookie.net/ballpit/images/1/11/Wraith_Ball.png/revision/latest?cb=20251023153249"},
    {"name": "Nosferatu", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/d0/Nosferatu_Ball.png/revision/latest?cb=20251023153249"},

    # Passives
    {"name": "Cornucopia", "icon": "https://static.wikia.nocookie.net/ballpit/images/b/be/Cornucopia.png/revision/latest?cb=20251023232034"},
    {"name": "Gracious Impaler", "icon": "https://static.wikia.nocookie.net/ballpit/images/a/ae/Gracious_Impaler.png/revision/latest?cb=20251023232035"},
    {"name": "Odiferous Shell", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/53/Odiferous_Shell.png/revision/latest?cb=20251023232035"},
    {"name": "Phantom Regalia", "icon": "https://static.wikia.nocookie.net/ballpit/images/d/da/Phantom_Regalia.png/revision/latest?cb=20251023232035"},
    {"name": "Soul Reaver", "icon": "https://static.wikia.nocookie.net/ballpit/images/9/9b/Soul_Reaver.png/revision/latest?cb=20251023232035"},
    {"name": "Tormentor's Mask", "icon": "https://static.wikia.nocookie.net/ballpit/images/2/2c/Tormenters_Mask.png/revision/latest?cb=20251023232035"},
    {"name": "Wings of the Anointed", "icon": "https://static.wikia.nocookie.net/ballpit/images/f/f8/Wings_Of_The_Anointed.png/revision/latest?cb=20251023232035"},
    {"name": "Deadeye's Cross", "icon": "https://static.wikia.nocookie.net/ballpit/images/5/51/Deadeyes_Cross.png/revision/latest?cb=20251023232035"},
]

# Create folder
os.makedirs("icons", exist_ok=True)

# Download icons
for item in items:
    if item['icon']:
        filename = os.path.join("icons", f"{item['name'].replace('/', '_')}.png")
        try:
            response = requests.get(item['icon'], stream=True)
            response.raise_for_status()
            with open(filename, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {item['name']}: {e}")
