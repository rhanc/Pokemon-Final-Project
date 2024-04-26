from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return [
    {
      "name": "Bulbasaur",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Ivysaur",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Vine Whip", "type": "Attack", "power": 45},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Venusaur",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Razor Leaf", "type": "Attack", "power": 55},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Charmander",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Charmeleon",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Charizard",
      "types": ["Fire", "Flying"],
      "weaknesses": ["Water", "Electric", "Rock"],
      "moves": [
        {"name": "Flamethrower", "type": "Attack", "power": 95},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Squirtle",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Wartortle",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Blastoise",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Hydro Pump", "type": "Attack", "power": 110},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Caterpie",
      "types": ["Bug"],
      "weaknesses": ["Fire", "Flying", "Rock"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "String Shot", "type": "Status", "effect": "Speed reduction"}
      ]
    },
    {
      "name": "Metapod",
      "types": ["Bug"],
      "weaknesses": ["Fire", "Flying", "Rock"],
      "moves": [
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Butterfree",
      "types": ["Bug", "Flying"],
      "weaknesses": ["Fire", "Electric", "Flying", "Rock"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Weedle",
      "types": ["Bug", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
      "moves": [
        {"name": "Poison Sting", "type": "Attack", "power": 15},
        {"name": "String Shot", "type": "Status", "effect": "Speed reduction"}
      ]
    },
    {
      "name": "Kakuna",
      "types": ["Bug", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
      "moves": [
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Beedrill",
      "types": ["Bug", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
      "moves": [
        {"name": "Twineedle", "type": "Attack", "power": 25},
        {"name": "Focus Energy", "type": "Status", "effect": "Critical hit ratio increase"}
      ]
    },
    {
      "name": "Pidgey",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Gust", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Pidgeotto",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Wing Attack", "type": "Attack", "power": 60},
        {"name": "Gust", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Pidgeot",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Sky Attack", "type": "Attack", "power": 140},
        {"name": "Gust", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Rattata",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Raticate",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Hyper Fang", "type": "Attack", "power": 80},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Spearow",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Fearow",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Drill Peck", "type": "Attack", "power": 80},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Ekans",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Wrap", "type": "Attack", "power": 15},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Arbok",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Acid", "type": "Attack", "power": 40},
        {"name": "Glare", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Pikachu",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Thunder Shock", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Raichu",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Thunderbolt", "type": "Attack", "power": 90},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Sandshrew",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Defense Curl", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Sandslash",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Slash", "type": "Attack", "power": 70},
        {"name": "Defense Curl", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Nidoran♀",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Nidorina",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Bite", "type": "Attack", "power": 60},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Nidoqueen",
      "types": ["Poison", "Ground"],
      "weaknesses": ["Water", "Ground", "Ice", "Psychic"],
      "moves": [
        {"name": "Body Slam", "type": "Attack", "power": 85},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Nidoran♂",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Nidorino",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Horn Attack", "type": "Attack", "power": 65},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Nidoking",
      "types": ["Poison", "Ground"],
      "weaknesses": ["Water", "Ground", "Ice", "Psychic"],
      "moves": [
        {"name": "Thrash", "type": "Attack", "power": 90},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Clefairy",
      "types": ["Fairy"],
      "weaknesses": ["Steel", "Poison"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Clefable",
      "types": ["Fairy"],
      "weaknesses": ["Steel", "Poison"],
      "moves": [
        {"name": "Double Slap", "type": "Attack", "power": 15},
        {"name": "Sing", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Vulpix",
      "types": ["Fire"],


      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Ninetales",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Fire Spin", "type": "Attack", "power": 35},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Jigglypuff",
      "types": ["Normal", "Fairy"],
      "weaknesses": ["Steel", "Poison"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Sing", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Wigglytuff",
      "types": ["Normal", "Fairy"],
      "weaknesses": ["Steel", "Poison"],
      "moves": [
        {"name": "Double Slap", "type": "Attack", "power": 15},
        {"name": "Sing", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Zubat",
      "types": ["Poison", "Flying"],
      "weaknesses": ["Electric", "Ice", "Psychic", "Rock"],
      "moves": [
        {"name": "Leech Life", "type": "Attack", "power": 20},
        {"name": "Supersonic", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Golbat",
      "types": ["Poison", "Flying"],
      "weaknesses": ["Electric", "Ice", "Psychic", "Rock"],
      "moves": [
        {"name": "Wing Attack", "type": "Attack", "power": 60},
        {"name": "Supersonic", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Oddish",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Absorb", "type": "Attack", "power": 20},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Gloom",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Acid", "type": "Attack", "power": 40},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Vileplume",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Petal Dance", "type": "Attack", "power": 120},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Paras",
      "types": ["Bug", "Grass"],
      "weaknesses": ["Fire", "Flying", "Bug", "Ice", "Poison"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Parasect",
      "types": ["Bug", "Grass"],
      "weaknesses": ["Fire", "Flying", "Bug", "Ice", "Poison"],
      "moves": [
        {"name": "Slash", "type": "Attack", "power": 70},
        {"name": "Spore", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Venonat",
      "types": ["Bug", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Venomoth",
      "types": ["Bug", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Rock"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Diglett",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Dugtrio",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Dig", "type": "Attack", "power": 80},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Meowth",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Persian",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Slash", "type": "Attack", "power": 70},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Psyduck",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
       

 {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Golduck",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Mankey",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Primeape",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Fury Swipes", "type": "Attack", "power": 18}
      ]
    },
    {
      "name": "Growlithe",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Bite", "type": "Attack", "power": 60},
        {"name": "Roar", "type": "Status", "effect": "Forced switch"}
      ]
    },
    {
      "name": "Arcanine",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Roar", "type": "Status", "effect": "Forced switch"}
      ]
    },
    {
      "name": "Poliwag",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Bubble", "type": "Attack", "power": 40},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Poliwhirl",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Poliwrath",
      "types": ["Water", "Fighting"],
      "weaknesses": ["Electric", "Grass", "Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Double Slap", "type": "Attack", "power": 15},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Abra",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Teleport", "type": "Status", "effect": "Escape from battle"}
      ]
    },
    {
      "name": "Kadabra",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Teleport", "type": "Status", "effect": "Escape from battle"}
      ]
    },
    {
      "name": "Alakazam",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Psybeam", "type": "Attack", "power": 65},
        {"name": "Teleport", "type": "Status", "effect": "Escape from battle"}
      ]
    },
    {
      "name": "Machop",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Karate Chop", "type": "Attack", "power": 50},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Machoke",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Low Kick", "type": "Attack", "power": 50},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Machamp",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Submission", "type": "Attack", "power": 80},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Bellsprout",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Vine Whip", "type": "Attack", "power": 45},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Weepinbell",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Razor Leaf", "type": "Attack", "power": 55},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Victreebel",
      "types": ["Grass", "Poison"],
      "weaknesses": ["Fire", "Flying", "Psychic", "Ice"],
      "moves": [
        {"name": "Razor Leaf", "type": "Attack", "power": 55},
        {"name": "Stun Spore", "type": "Status", "effect": "Paralysis"}
      ]
    },
    {
      "name": "Tentacool",
      "types": ["Water", "Poison"],
      "weaknesses": ["Electric", "Ground", "Psychic"],
      "moves": [
        {"name": "Poison Sting", "type": "Attack", "power": 15},
        {"name": "Supersonic", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Tentacruel",
      "types": ["Water", "Poison"],
      "weaknesses": ["Electric", "Ground", "Psychic"],
      "moves": [
        {"name": "Acid", "type": "Attack", "power": 40},
        {"name": "Supersonic", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Geodude",
      "types": ["Rock", "Ground"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Defense Curl", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Graveler",
      "types": ["Rock", "Ground"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground"],
      "moves": [
        {"name": "Rock Throw", "type": "Attack", "power": 50},
        {"name": "Defense Curl", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Golem",
      "types": ["Rock", "Ground"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground"],
      "moves": [
        {"name": "Rock Throw", "type": "Attack", "power": 50},
        {"name": "Defense Curl", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Ponyta",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Rapidash",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Stomp", "type": "Attack", "power": 65},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Slowpoke",
      "types": ["Water", "Psychic"],
      "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Slowbro",
      "types": ["Water", "Psychic"],
      "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Magnemite",
      "types": ["Electric", "Steel"],
      "weaknesses": ["Fire", "Fighting", "Ground"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Thunder Shock", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Magneton",
      "types": ["Electric", "Steel"],
      "weaknesses": ["Fire", "Fighting", "Ground"],
      "moves": [
        {"name": "Thunder Shock", "type": "Attack", "power": 40},
        {"name": "Sonic Boom", "type": "Attack", "power": 90}
      ]
    },
    {
      "name": "Farfetch'd",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Doduo",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Dodrio",
      "types": ["Normal", "Flying"],
      "weaknesses": ["Electric", "Ice", "Rock"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Seel",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Headbutt", "type": "Attack", "power": 70},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Dewgong",
      "types": ["Water", "Ice"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Rock"],
      "moves": [
        {"name": "Headbutt", "type": "Attack", "power": 70},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Grimer",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Disable", "type": "Status", "effect": "Move locking"}
      ]
    },
    {
      "name": "Muk",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Sludge", "type": "Attack", "power": 65},
        {"name": "Disable", "type": "Status", "effect": "Move locking"}
      ]
    },
    {
      "name": "Shellder",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Withdraw", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Cloyster",
      "types": ["Water", "Ice"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Rock"],
      "moves": [
        {"name": "Clamp", "type": "Attack", "power": 35},
        {"name": "Withdraw", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Gastly",
      "types": ["Ghost", "Poison"],
      "weaknesses": ["Ghost", "Dark", "Psychic"],
      "moves": [
        {"name": "Lick", "type": "Attack", "power": 30},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Haunter",
      "types": ["Ghost", "Poison"],
      "weaknesses": ["Ghost", "Dark", "Psychic"],
      "moves": [
        {"name": "Lick", "type": "Attack", "power": 30},
        {"name": "Confuse Ray", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Gengar",
      "types": ["Ghost", "Poison"],
      "weaknesses": ["Ghost", "Dark", "Psychic"],
      "moves": [
        {"name": "Lick", "type": "Attack", "power": 30},
        {"name": "Night Shade", "type": "Attack", "power": 1}
      ]
    },
    {
      "name": "Onix",
      "types": ["Rock", "Ground"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Screech", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Drowzee",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Hypno",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Krabby",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Bubble", "type": "Attack", "power": 40},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Kingler",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Bubble", "type": "Attack", "power": 40},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Voltorb",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Sonic Boom", "type": "Attack", "power": 90}
      ]
    },
    {
      "name": "Electrode",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Sonic Boom", "type": "Attack", "power": 90}
      ]
    },
    {
      "name": "Exeggcute",
      "types": ["Grass", "Psychic"],
      "weaknesses": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Barrage", "type": "Attack", "power": 15},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Exeggutor",
      "types": ["Grass", "Psychic"],
      "weaknesses": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Hypnosis", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Cubone",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Bone Club", "type": "Attack", "power": 65},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Marowak",
      "types": ["Ground"],
      "weaknesses": ["Water", "Grass", "Ice"],
      "moves": [
        {"name": "Bonemerang", "type": "Attack", "power": 50},
        {"name": "Growl", "type": "Status", "effect": "Attack reduction"}
      ]
    },
    {
      "name": "Hitmonlee",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Double Kick", "type": "Attack", "power": 30},
        {"name": "High Jump Kick", "type": "Attack", "power": 130}
      ]
    },
    {
      "name": "Hitmonchan",
      "types": ["Fighting"],
      "weaknesses": ["Flying", "Psychic", "Fairy"],
      "moves": [
        {"name": "Comet Punch", "type": "Attack", "power": 18},
        {"name": "Sky Uppercut", "type": "Attack", "power": 85}
      ]
    },
    {
      "name": "Lickitung",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Lick", "type": "Attack", "power": 30},
        {"name": "Supersonic", "type": "Status", "effect": "Confusion"}
      ]
    },
    {
      "name": "Koffing",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Smog", "type": "Attack", "power": 30}
      ]
    },
    {
      "name": "Weezing",
      "types": ["Poison"],
      "weaknesses": ["Ground", "Psychic"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Smog", "type": "Attack", "power": 30}
      ]
    },
    {
      "name": "Rhyhorn",
      "types": ["Ground", "Rock"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
      "moves": [
        {"name": "Horn Attack", "type": "Attack", "power": 65},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Rhydon",
      "types": ["Ground", "Rock"],
      "weaknesses": ["Water", "Grass", "Ice", "Fighting", "Ground", "Steel"],
      "moves": [
        {"name": "Horn Attack", "type": "Attack", "power": 65},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Chansey",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Double Slap", "type": "Attack", "power": 15},
        {"name": "Sing", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Tangela",
      "types": ["Grass"],
      "weaknesses": ["Fire", "Flying", "Ice", "Poison", "Bug"],
      "moves": [
        {"name": "Vine Whip", "type": "Attack", "power": 45},
        {"name": "Bind", "type": "Attack", "power": 15}
      ]
    },
    {
      "name": "Kangaskhan",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Comet Punch", "type": "Attack", "power": 18},
        {"name": "Rage", "type": "Status", "effect": "Attack increase"}
      ]
    },
    {
      "name": "Horsea",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Bubble", "type": "Attack", "power": 40},
        {"name": "SmokeScreen", "type": "Status", "effect": "Accuracy reduction"}
      ]
    },
    {
      "name": "Seadra",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Bubble", "type": "Attack", "power": 40},
        {"name": "SmokeScreen", "type": "Status", "effect": "Accuracy reduction"}
      ]
    },
    {
      "name": "Goldeen",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Seaking",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Horn Attack", "type": "Attack", "power": 65},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Staryu",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Starmie",
      "types": ["Water", "Psychic"],
      "weaknesses": ["Electric", "Grass", "Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Mr. Mime",
      "types": ["Psychic", "Fairy"],
      "weaknesses": ["Ghost", "Steel", "Poison"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Barrier", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Scyther",
      "types": ["Bug", "Flying"],
      "weaknesses": ["Fire", "Electric", "Ice", "Flying", "Rock"],
      "moves": [
        {"name": "Quick Attack", "type": "Attack", "power": 40},
        {"name": "Swords Dance", "type": "Status", "effect": "Attack increase"}
      ]
    },
    {
      "name": "Jynx",
      "types": ["Ice", "Psychic"],
      "weaknesses": ["Fire", "Bug", "Rock", "Ghost", "Dark", "Steel"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Lovely Kiss", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Electabuzz",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Quick Attack", "type": "Attack", "power": 40},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Magmar",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Pinsir",
      "types": ["Bug"],
      "weaknesses": ["Fire", "Flying", "Rock"],
      "moves": [
        {"name": "Vice Grip", "type": "Attack", "power": 55},
        {"name": "Focus Energy", "type": "Status", "effect": "Critical hit ratio increase"}
      ]
    },
    {
      "name": "Tauros",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Magikarp",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Splash", "type": "Status", "effect": "No effect"},
        {"name": "Tackle", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Gyarados",
      "types": ["Water", "Flying"],
      "weaknesses": ["Electric", "Rock"],
      "moves": [
        {"name": "Bite", "type": "Attack", "power": 60},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Lapras",
      "types": ["Water", "Ice"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Rock"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Sing", "type": "Status", "effect": "Sleep"}
      ]
    },
    {
      "name": "Ditto",
      "types": ["Normal"],
      "weaknesses": [],
      "moves": [
        {"name": "Transform", "type": "Status", "effect": "Copy opponent's stats and moves"}
      ]
    },
    {
      "name": "Eevee",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Vaporeon",
      "types": ["Water"],
      "weaknesses": ["Electric", "Grass"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Jolteon",
      "types": ["Electric"],
      "weaknesses": ["Ground"],
      "moves": [
        {"name": "Thunder Shock", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Flareon",
      "types": ["Fire"],
      "weaknesses": ["Water", "Rock", "Ground"],
      "moves": [
        {"name": "Ember", "type": "Attack", "power": 40},
        {"name": "Tail Whip", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Porygon",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Conversion", "type": "Status", "effect": "Change type to opponent's last move"}
      ]
    },
    {
      "name": "Omanyte",
      "types": ["Rock", "Water"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Withdraw", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Omastar",
      "types": ["Rock", "Water"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
      "moves": [
        {"name": "Water Gun", "type": "Attack", "power": 40},
        {"name": "Withdraw", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Kabuto",
      "types": ["Rock", "Water"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Kabutops",
      "types": ["Rock", "Water"],
      "weaknesses": ["Electric", "Grass", "Fighting", "Ground"],
      "moves": [
        {"name": "Scratch", "type": "Attack", "power": 40},
        {"name": "Harden", "type": "Status", "effect": "Defense increase"}
      ]
    },
    {
      "name": "Aerodactyl",
      "types": ["Rock", "Flying"],
      "weaknesses": ["Water", "Electric", "Ice", "Rock", "Steel"],
      "moves": [
        {"name": "Wing Attack", "type": "Attack", "power": 35},
        {"name": "Agility", "type": "Status", "effect": "Speed increase"}
      ]
    },
    {
      "name": "Snorlax",
      "types": ["Normal"],
      "weaknesses": ["Fighting"],
      "moves": [
        {"name": "Tackle", "type": "Attack", "power": 40},
        {"name": "Amnesia", "type": "Status", "effect": "Special Defense increase"}
      ]
    },
    {
      "name": "Articuno",
      "types": ["Ice", "Flying"],
      "weaknesses": ["Fire", "Electric", "Steel", "Rock"],
      "moves": [
        {"name": "Gust", "type": "Attack", "power": 40},
        {"name": "Mist", "type": "Status", "effect": "Prevents stat reduction"}
      ]
    },
    {
      "name": "Zapdos",
      "types": ["Electric", "Flying"],
      "weaknesses": ["Ice", "Rock"],
      "moves": [
        {"name": "Peck", "type": "Attack", "power": 35},
        {"name": "ThunderShock", "type": "Attack", "power": 40}
      ]
    },
    {
      "name": "Moltres",
      "types": ["Fire", "Flying"],
      "weaknesses": ["Water", "Electric", "Rock"],
      "moves": [
        {"name": "Wing Attack", "type": "Attack", "power": 35},
        {"name": "Agility", "type": "Status", "effect": "Speed increase"}
      ]
    },
    {
      "name": "Dratini",
      "types": ["Dragon"],
      "weaknesses": ["Ice", "Dragon", "Fairy"],
      "moves": [
        {"name": "Wrap", "type": "Attack", "power": 15},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Dragonair",
      "types": ["Dragon"],
      "weaknesses": ["Ice", "Dragon", "Fairy"],
      "moves": [
        {"name": "Wrap", "type": "Attack", "power": 15},
        {"name": "Leer", "type": "Status", "effect": "Defense reduction"}
      ]
    },
    {
      "name": "Dragonite",
      "types": ["Dragon", "Flying"],
      "weaknesses": ["Ice", "Rock", "Dragon", "Fairy"],
      "moves": [
        {"name": "Wing Attack", "type": "Attack", "power": 35},
        {"name": "Agility", "type": "Status", "effect": "Speed increase"}
      ]
    },
    {
      "name": "Mewtwo",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Confusion", "type": "Attack", "power": 50},
        {"name": "Amnesia", "type": "Status", "effect": "Special Defense increase"}
      ]
    },
    {
      "name": "Mew",
      "types": ["Psychic"],
      "weaknesses": ["Bug", "Ghost", "Dark"],
      "moves": [
        {"name": "Pound", "type": "Attack", "power": 40},
        {"name": "Transform", "type": "Status", "effect": "Copy opponents stats and moves"}
      ]
    }
  ]
    
    